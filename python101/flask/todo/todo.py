#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#

"""

"""
from datetime import datetime
from flask import flash, redirect, url_for, request
from flask import Flask, g
from flask import render_template
from flask import session
import os
import sqlite3

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY='bardzosekrtnawartosc',
    DATABASE=os.path.join(app.root_path, 'db.sqlite'),
    SITE_NAME='Moje zadania'
    ))

def get_db():
    """Funkcja tworząca połączenie z bazą danych"""
    if not g.get('db'): # jeżeli brak połączenia, to je tworzymy
        con = sqlite3.connect(app.config['DATABASE'])
        con.row_factory = sqlite3.Row
        g.db = con # zapisujemy połączenie w kontekście aplikacji
    return g.db # zwracamy połączenie z bazą

@app.teardown_appcontext
def close_db(error):
    """Zamykamy połączenie z bazą"""
    if g.get('db'):
        g.db.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/zadania', methods=['GET', 'POST'])
def zadania():
    error = None
    user_id = 0
    if 'user_id' in session:
        user_id = session['user_id']
    if request.method == 'POST':
        zadanie = request.form['zadanie'].strip()
        if len(zadanie) > 0:
            zrobione = '0'
            data_pub = datetime.now()
            db = get_db()
            db.execute('INSERT INTO zadania VALUES (?, ?, ?, ?, ?);',
                    [None, zadanie, zrobione, data_pub, user_id])
            db.commit()
            flash('Dodano nowe zadanie.'+str(user_id))
            return redirect(url_for('zadania'))

        error = 'Nie możesz dodać pustego zadania!' # komunikat o błędzie

    db = get_db()
    kursor = db.execute('SELECT * FROM zadania WHERE uzy_id=? ORDER BY data_pub DESC;', [user_id])
    zadania = kursor.fetchall()
    return render_template('zadania_lista.html', zadania=zadania, error=error)

@app.route('/zrobione', methods=['POST'])
def zrobione():
    """Zmiana statusu zadania na wykonanie."""
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('UPDATE zadania SET zrobione=1 WHERE id=?', [zadanie_id])
    db.commit()
    flash('Zmieniono status zadania.')
    return redirect(url_for('zadania'))

@app.route('/usun', methods=['POST'])
def usun():
    zadanie_id = request.form['id']
    db = get_db()
    db.execute('DELETE FROM zadania WHERE id=?', [zadanie_id])
    db.commit()
    flash('Usunięte zadanie')
    return redirect(url_for('zadania'))

@app.route('/zaloguj', methods=['POST'])
def zaloguj():
    session['username'] = request.form['nick']
    nick = session['username']
    db = get_db()
    kursor = db.execute('SELECT id from uzytkownik WHERE nick=?', [nick])
    uzy_id = kursor.fetchone()
    if uzy_id == None:
        session['user_id'] = 0
        #flash("You must enter a valid user name!")
        return redirect(url_for('index'))
    else:
        session['user_id'] = uzy_id[0]
        return redirect(url_for('zadania'))



app.run(debug=True)
