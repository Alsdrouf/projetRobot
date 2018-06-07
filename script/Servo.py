#!:usr/bin/env python
# -*- coding: UTF-8 -*-#enable debugging
import RPi.GPIO as GPIO
import time

file= "Log.txt"
Log=open(file, "r")
Store=Log.readlines()
Ligne=len(open(file, "r").readlines())
def master(BROCHE1, BROCHE2, BROCHE3, BROCHE4, PAUSE):
	phrase=Store[Ligne-1]
	car2=0
	BROCHE=2
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(BROCHE1, GPIO.OUT)
	GPIO.setup(BROCHE2, GPIO.OUT)
	GPIO.setup(BROCHE3, GPIO.OUT)
	GPIO.setup(BROCHE4, GPIO.OUT)
	GPIO.setwarnings(False)
	for car in range(len(phrase)):
		if phrase[car]== ";":
			car2=car+1
			while (phrase[car2]!=";") and (car2!=len(phrase)-1):
				car2=car2+1
			if BROCHE==2: #Rotation Avant-Arrière
				pwm=GPIO.PWM(BROCHE2, 100)
				pwm.start(5)
				angle=float(phrase[car+1:car2])/10+5
				pwm.ChangeDutyCycle(angle)
				time.sleep(PAUSE)
				BROCHE=BROCHE+1
				print (angle)
			elif BROCHE==3: #Pince Ouvert-Fermer
				pwm=GPIO.PWM(BROCHE3, 100)
				pwm.start(5)
				angle=float(phrase[car+1:car2])/10+5
				pwm.ChangeDutyCycle(angle)
				time.sleep(PAUSE)
				BROCHE=BROCHE+1
				print (angle)
			elif BROCHE==4: #Rotation Gauche-Droite
				pwm=GPIO.PWM(BROCHE4, 100)
				pwm.start(5)
				angle=float(phrase[car+1:car2])/10+5
				pwm.ChangeDutyCycle(angle)
				time.sleep(PAUSE)
				print (angle)
		elif phrase[car]=="]": #Rotation Bas-Haut
			car2=car+1
			while phrase[car2]!=";":
				car2=car2+1
			pwm=GPIO.PWM(BROCHE1, 100)
			pwm.start(5)
			angle=float(phrase[car+2:car2])/10+5
			pwm.ChangeDutyCycle(angle)
			time.sleep(PAUSE)
			print (angle)
	GPIO.cleanup()
master(17, 27, 22, 16, 1)
Log.close()
