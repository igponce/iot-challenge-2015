#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
powercontrol.py

Apaga / Enciende el rele conectado al puerto GPIO
en funcion de la programacion hecha en el servidor web.

Este programa debe ejecutarse desde el crontab en Linux
para que se mantenga al programacion.
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

import pickle
import datetime
import rpirelay
from commonconfig import *

"""
   Formato de configuracion:
   programacion = { 'estado': "always_on|always_off|prog",
                     'start': hora_inicio_programacion (hora: no datetime), 
                       'end': hora_fin_programacion,
               'randomdelay': max_segundos_inicio_programacion
                    'tarifa': "2.0.DHA (por ejemplo)" 
                  }
"""

# read config

fp = open( CONFIG_FILE, 'rb')
programacion = pickle.load( fp )
fp.close()

if programacion['estado'] ==  "prog":
	dt = datetime.datetime.now()

	if ( dt.hour >= programacion['start'] ) and ( dt.hour <= programacion['end'] ):
		rpirelay.enable(programacion['randomdelay']) # Ojo: Puede haber microcortes?
	else:
		rpirelay.disable()

elif programacion['estado']  ==  "always_off":
		rpirelay.disable()

else: # "always_on" es el mejor estado por defecto (enchufe no kaputt)
	rpirelay.enable(0) # No delay

# ToDo: Enviar mensaje a Azure en los cambios de estado, al ejecutarse, etc. para analiticas.