#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging

import cgi
first=1
file = "Potentiometre.txt"
Log=open(file,"r")
Store = Log.readlines()
Ligne=len(open(file,"r").readlines())
print "Content-type:text/html\r\n\r\n"

print '<html>'
print '<head>'
print '<meta charset="UTF-8">'
print '</head>'
print '<body>'
print '<canvas id="Courbe" width="1124" height="440" style="border:1px solid #000000"></canvas>'
print '<table border="1">'
print '<caption>Log capteur de lumière: '+str(Ligne)+' ligne(s)</caption>'
print '<thead>'
print '<tr>'
print '<th>Angle:</th>'
print '<th>Valeur:</th>'
print '</tr>'
print '</thead>'
print '<tbody>'
for loop in range(Ligne):
	phrase = Store[Ligne-1]
	#print ''+str(phrase)+''
	Ligne=Ligne-1
	car2=0
	for car in range(len(phrase)):
		if phrase[car] == ":":
			car2=car+1
			while (phrase[car2]!=";") and (car2!=len(phrase)-1):
				car2=car2+1
			print '<td>'
			print ''+str(phrase[car+1:car2])+''
			print '</td>'
	print '</tr>'
print '</tbody>'
print '</table>'
print '<script>'
print 'var c=document.getElementById("Courbe");'
print 'var ctx =c.getContext("2d");'
print 'ctx.beginPath();'
print 'ctx.moveTo(100,10);'
print 'ctx.lineTo(100,350)'
print 'ctx.lineTo(1124,350)'
print 'ctx.moveTo(100,10)'
print 'ctx.lineTo(1124,10)'
print 'ctx.moveTo(100,350)'
print 'ctx.font="10px Arial"'
print 'ctx.fillText("Angle",50,20)'
print 'ctx.fillText("Valeur",1090,370)'
valeur=0
y=355
for loop in range(35):
	print 'ctx.fillText("'+str(valeur)+'",80,'+str(y)+')'
	y=y-10
	valeur=valeur+5
valeur=50
x=140
for loop in range(20):
	print 'ctx.fillText("'+str(valeur)+'",'+str(x)+',360)'
	valeur=valeur+50
	x=x+50
Ligne2=0
Ligne=len(open(file,"r").readlines())
for loop in range(Ligne):
	Ligne2=Ligne2+1
	phrase=Store[Ligne2-1]
	car2=0
	for car in range(len(phrase)):
		if phrase[car]== ":":
			car2=car+1
			while (phrase[car2]!=";") and (car2!=len(phrase)-1):
				car2=car2+1
			if first == 1:
				first=0
				y=350-2*int(phrase[car+1:car2])
			else:
				first=1
				x=100+int(phrase[car+1:car2])
	print 'ctx.lineTo('+str(x)+','+str(y)+')'
print 'ctx.stroke();'
print 'ctx.closePath();'
print '</script>'
print '</body>'
print '</html>'
Log.close()
