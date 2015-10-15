#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

rpirelay.py 

Modulo que conecta / desconecta el rele a traves del pin GPIO.
Se hace modulo aparte para depurarlo en windows sin tener que usar
una raspberry ni tocar codigo de powercontrol (que es lo bastante simple)

----------------------------------------------------------------------------------

Copyright (C) 2015 Iñigo Gonzalez Ponce <igponce (at) gmail (dot) youknowwhat>

Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense,
 and/or sell copies of the Software, and to permit persons to whom the Software
 is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included 
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
DEALINGS IN THE SOFTWARE
"""

import RPi.GPIO as gpio
from time import sleep
from random import randint

GPIO_RELAY_PIN = 23 # Provisional

def enable ( randomdelay = 5):

	set_delay = randomdelay if randomdelay < 90 else 90 # limitamos a 90 segundos
	if (set_delay > 0):
		sleep(randint(1,randomdelay))

	gpio.setwarnings(False)
	gpio.setmode(gpio.BCM)
	gpio.setup(GPIO_RELAY_PIN,gpio.OUT)
	gpio.out(GPIO_RELAY_PIN,gpio.HIGH)

def disable():
	gpio.setwarnings(False)
	gpio.setmode(gpio.BCM)
	gpio.setup(GPIO_RELAY_PIN,gpio.OUT)
	gpio.out(GPIO_RELAY_PIN,gpio.LOW)
