#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

commonconfig.py

Configuracion comun a la aplicacion web y el controlador de reles de la raspberry

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

# Configuracion de la aplicación y estado

CONFIG_FILE = "config.pickle"

# Azure soporta HTTPS y HTTP - en principio basta con usar HTTP sin cifrar
# En caso de problemas con la red (caches transparentes y similares)
# se puede usar https aunque cargue más la cpu y la pila de la raspbery

ENERGY_PRICE_URL = "http://iotenergydemo.blob.core.windows.net/energyprice/precios.pickle"
ENERGY_PRICE_FILE = "energy.pickle"


# Fichero con programacion / estado de la configuracion

PROGRAM_FILE = 'program.pickle'

#EOF#