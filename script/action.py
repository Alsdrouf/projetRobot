#!/usr/bin/env python
# -*- coding: UTF-8 -*-# enable debugging
import cgi
import time
"""import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setwarnings(False)
pwm=GPIO.PWM(17,100)
pwm.start(5)
angle_choisi=float(20)/10+5
pwm.ChangeDutyCycle(angle_choisi)
time.sleep(1)
GPIO.cleanup()"""
formData = cgi.FieldStorage()
angle= formData.getvalue('Bras_bas_haut')
angle_deux=formData.getvalue('Bras_avant_arriere')
angle_pince=formData.getvalue('pince')
angle_rota=formData.getvalue('motor_base')
Log=open("Log.txt","a")
try:
	angle=int(angle)
except:
	pass
else:
	Log.write("["+str(time.asctime( time.localtime(time.time())))+"] "+str(angle)+";"+str(angle_deux)+";"+str(angle_pince)+";"+str(angle_rota)+"\n")
Log.close()
print "Content-type:text/html\r\n\r\n"

print '<html>'
print '<head>'
print '<meta charset="UTF-8">'
print '</head>'
print '<body bgcolor="#C3E0EC">'
print '<form style=color:DodgerBlue action="Courbe.py">'
print '<button class="float-left submit-button">Courbe photosensor</button>'
print '</form>'
print '<form style=color:DodgerBlue method="post" class=inline action="Log.py">'
print '<button class="float-left submit-button" >Log</button>'
print '<br>'
print 'Rotation Gauche-Droite : '
print formData.getvalue('motor_base')
print '<br>'
print 'Rotation Bas-Haut : '
print formData.getvalue('Bras_bas_haut')
print '<br>'
print 'Rotation Avant-Arrière : '
print formData.getvalue('Bras_avant_arriere')
print '<br>'
print 'Pince Ouverte-Fermer : '
print formData.getvalue('pince')
print '</form>'
print '<canvas id="vue_normal" width="800" height="300" style="border:1px solid #000000"></canvas>'
print '<canvas id="vue_dessus" width="800" height="500" style="border:1px solid #000000"></canvas>'
print '<script>'
print 'var canvas = document.getElementById("vue_normal")'
print 'var ctx = canvas.getContext("2d");'
print 'ctx.beginPath();'
print 'ctx.arc(150,240,60,0,2*Math.PI);'
print 'ctx.moveTo(150,240);'
print 'ctx.lineTo(150,300);'
print 'ctx.moveTo(150,240);'
print 'ctx.lineTo(150,180);'
print 'ctx.moveTo(150,240);'
print 'ctx.lineTo(210,240);'
print 'ctx.moveTo(150,240);'
print 'ctx.lineTo(90,240);'
print 'ctx.stroke();'
print 'ctx.moveTo(210,240);'
print 'ctx.lineTo(400,240);'
print 'ctx.stroke();'
print 'ctx.beginPath();'
print 'ctx.arc(460,240,60,0,2*Math.PI);'
print 'ctx.moveTo(460,240);'
print 'ctx.lineTo(460,300);'
print 'ctx.moveTo(460,240);'
print 'ctx.lineTo(460,180);'
print 'ctx.moveTo(460,240);'
print 'ctx.lineTo(400,240);'
print 'ctx.moveTo(460,240);'
print 'ctx.lineTo(520,240);'
print 'ctx.stroke();'
print 'ctx.moveTo(150,180);'
print 'ctx.lineTo(460,180);'
print 'ctx.stroke();'
print 'ctx.moveTo(305,180);'
print 'ctx.lineTo(155*Math.cos('+str(angle)+'/180*Math.PI)+305,-155*Math.sin('+str(angle)+'/180*Math.PI)+180);'
print 'ctx.moveTo(155*Math.cos('+str(angle)+'/180*Math.PI)+305,-155*Math.sin('+str(angle)+'/180*Math.PI)+180);'
print 'ctx.lineTo((155*Math.cos('+str(angle)+'/180*Math.PI)+305)+155*Math.cos('+str(angle_deux)+'/180*Math.PI),(-155*Math.sin('+str(angle)+'/180*Math.PI)+180)+155*Math.sin('+str(angle_deux)+'/180*Math.PI));'
print 'ctx.moveTo((155*Math.cos('+str(angle)+'/180*Math.PI)+305)+155*Math.cos('+str(angle_deux)+'/180*Math.PI),(-155*Math.sin('+str(angle)+'/180*Math.PI)+180)+155*Math.sin('+str(angle_deux)+'/180*Math.PI));'
print 'var x=(155*Math.cos('+str(angle)+'/180*Math.PI)+305)+155*Math.cos('+str(angle_deux)+'/180*Math.PI);'
print 'var y=(-155*Math.sin('+str(angle)+'/180*Math.PI)+180)+155*Math.sin('+str(angle_deux)+'/180*Math.PI);'
print 'ctx.lineTo(x+50*Math.cos('+str(angle_pince)+'/180*Math.PI), y+50*Math.sin('+str(angle_pince)+'/180*Math.PI));'
print 'ctx.lineTo(x+50*Math.cos('+str(angle_pince)+'/180*Math.PI)+10, y+50*Math.sin('+str(angle_pince)+'/180*Math.PI)-10);'
print 'ctx.moveTo(x, y);'
print 'ctx.lineTo(x+50*Math.cos('+str(angle_pince)+'/180*Math.PI), y-50*Math.sin('+str(angle_pince)+'/180*Math.PI));'
print 'ctx.lineTo(x+50*Math.cos('+str(angle_pince)+'/180*Math.PI)+10, y-50*Math.sin('+str(angle_pince)+'/180*Math.PI)+10);'
print 'ctx.stroke();'
print 'var canvas = document.getElementById("vue_dessus");'
print 'var ctx = canvas.getContext("2d");'
print 'ctx.rect(250,150,300,200);'
print 'ctx.rect(250,150,100,-50);'
print 'ctx.rect(550,150,-100,-50);'
print 'ctx.rect(550,350,-100,50);'
print 'ctx.rect(250,350,100,50);'
print 'ctx.moveTo(400,250);'
print 'var longueur_bras=Math.sqrt(Math.pow((x-305),2)+Math.pow((0),2));'
print 'ctx.lineTo(longueur_bras*Math.cos(('+str(angle_rota)+'-90)/180*Math.PI)+400,longueur_bras*Math.sin(('+str(angle_rota)+'-90)/180*Math.PI)+250);'
print 'ctx.stroke();'
print '</script>'
print '<address>Open-source:<a href=https://github.com/Alsdrouf/projetRobot>https://github.com/Alsdrouf/projetRobot</a></address>'
print '</body>'
print '</html>'
