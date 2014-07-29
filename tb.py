#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Dieses Programm erstellt für den aktuellen Tag -- oder einen anderen -- eine Tagesdatei für Notizen.

Bei Erstellung einer Datei für heute oder in der Zukunft wird bis zu 4 Tage zurück nach einem Todomarker
gesucht, um mögliche Todos in die neue Datei zu übernehmen.

Der normale Aufruf ist: tb
Dies erstellt eine Datei für heute, außer sie existiert bereits.

Aufruf für Tage in der Vergangenheit oder Zukunft: tb +3  (Aufruf freitags für Montag)
Oder auch mit negativen Zahlen.

(C) 2014 by Tjabo Vierbücher
"""
import os
import os.path
import time
from datetime import date
import sys
import subprocess

import locale
locale.setlocale( locale.LC_TIME, 'de_DE' )
# todo: tb -n

# todo find homedir
tbpath = "Tagebuch"
editor = "vim"
daysAdd = 0
if len(sys.argv) > 1:
	daysAdd = int( sys.argv[1] )

now = time.time()
now = now + (8600 * daysAdd)
nowDate = date.fromtimestamp( now )
todo = '';

def makeFilename(dir, mydate):
	return os.path.join( dir, mydate.strftime("%Y-%m-%d-%a.txt") )

# ensure the year directory exists:
currentDir = os.path.join( tbpath, nowDate.strftime("%Y") )
if not os.path.exists( currentDir ):
	os.makedirs( currentDir )

currentFile = makeFilename( currentDir, nowDate )
if os.path.isfile( currentFile ):
	print "Datei existiert schon: %s" % (currentFile, )

else:
	if daysAdd >= 0:  # nur wenn nicht in der Vergangenheit gespielt wird:
		for days in (1,2,3,4):	# zurück in der zeit nach einem file suchen, und von dem den todo-block übernehmen:
			pastDate = date.fromtimestamp(now - (86400*days))
			pastFile = os.path.join( currentDir, pastDate.isoformat() ) + ".txt"
			if os.path.isfile( pastFile ):
				f = open(pastFile, 'r') 		# Lese optionalen Todo-Block aus, zum Übernehmn in die neue Datei:
				data = f.read()
				f.close()
				todoPos = data.find('%Todo:')
				if todoPos > -1:
					todo = data[ todoPos: ]
				break;

# Erzeuge neue Tagesdatei:
f = open(currentFile, 'w')
f.write( nowDate.strftime("%d.%m.%Y (%A)\n\n") )
for i in range(7):
	f.write( "( ) \n" )
if len(todo):
	f.write( "\n" + todo )
f.close()

print "Neue Datei: %s" % (currentFile, )
subprocess.call( [editor, currentFile] )
