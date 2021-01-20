#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

"""

"""
from flask import Flask
from flask import render_template
from flask import request, redirect, url_for, flash

app = Flask(__name__)

# konfiguracja aplikacji
app.config.update(dict(
    SECRET_KEY='bardzosekretnawartosc',
    ))

# lista pytan
DANE = [{
    'pytanie': 'Stolica Hiszpani, to:',
    'odpowiedzi': ['Madryt', 'Warszawa', 'Barcelona'],
    'odpok': 'Madryt'},
    {
    'pytanie': 'Objętość sześcianu o boku 6cm, wynosi:',
    'odpowiedzi': ['36', '216', '18'],
    'odpok': '216'},
    {
    'pytanie': 'Symbole pierwiastka Helu, to:',
    'odpowiedzi': ['Fe', 'H', 'He'],
    'odpok': 'He'},
    ]
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        punkty = 0
        odpowiedzi = request.form

        for pnr, odp in odpowiedzi.items():
            if odp == DANE[int(pnr)]['odpok']:
                punkty += 1

        flash('Liczba poprawnych odpowiedzi, to: {0}'.format(punkty))
        return redirect(url_for('index'))
    #return 'Cześć, tu Python!'
    return render_template('index.html', pytania=DANE)

if __name__ == '__main__':
    app.run(debug=True)
