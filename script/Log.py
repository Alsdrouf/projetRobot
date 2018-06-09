#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import cgi
file = "Log.txt"
Log=open(file,"r")
Store = Log.readlines()
Ligne=len(open(file,"r").readlines())
print "Content-type:text/html\r\n\r\n"

print '<html>'
print '<head>'
print '<meta charset="UTF-8">'
print '</head>'
print '<body>'
print '<table border="1">'
print '<caption>Log des Servo-moteur: '+str(Ligne)+' ligne(s)</caption>'
print '<thead>'
print '<tr>'
print '<th>Date:</th>'
print '<th>Rota. Bas-Haut:</th>'
print '<th>Rota. Avant-Arrière</th>'
print '<th>Pince Ouvert-Fermer</th>'
print '<th>Rota. Gauche-Droite</th>'
print '</tr>'
print '</thead>'
print '<tbody>'
for loop in range(Ligne):
	phrase = Store[Ligne-1]
	Ligne=Ligne-1
	car2=0
	print '<tr>'
	for car in range(len(phrase)):
		#print ''+str(phrase[car])+''
		if phrase[car] == ";":
			car2=car+1
			while (phrase[car2]!=";") and (car2!=len(phrase)-1):
				car2=car2+1
			print '<td>'
			print ''+str(phrase[car+1:car2])+''
			print '</td>'
		elif phrase[car] == "]":
			car2=car+1
			print '<td>'
			print ''+str(phrase[0:car])+''
			print '</td>'
			while phrase[car2]!=";":
				car2=car2+1
			print '<td>'
			print ''+str(phrase[car+2:car2])+''
			print '</td>'
	print '</tr>'
print '</tbody>'
print '</table>'
print '<address>Open-source:<a href=https://github.com/Alsdrouf/projetRobot>https://github.com/Alsdrouf/projetRobot</a></address>'
print '</body>'
print '</html>'
Log.close()
