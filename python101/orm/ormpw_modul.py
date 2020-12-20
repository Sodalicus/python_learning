#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 Paweł Krzemiński 
#
# Distributed under terms of the MIT license.

"""

"""
import csv,os
def getdata(csvfile):
    if os.path.isfile(csvfile):
        with open(csvfile, 'r') as file:
            spamreader = csv.reader(file, delimiter=',')
            data = []
            for row in spamreader:
                dicks = {}
                dicks['imie']=row[0]
                dicks['nazwisko']=row[1]
                dicks['klasa']=row[2]

                data.append(dicks)
            return data
