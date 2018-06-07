#!/usr/bin/python
# -*- coding: utf-8 -*-

import spidev
import time

spi=spidev.SpiDev()
spi.open(0,0)

def ReadChannel(channel):
	adc=spi.xfer2([1,(8+channel)<<4,0])
	data=((adc[1]&3)<<8)+adc[2]
	return data

while True:
	valeur1=ReadChannel(0)
	valeur2=ReadChannel(1)
	print ("Valeur une: "+str(valeur1)+", Valeur deux: "+str(valeur2))
	time.sleep(1)
