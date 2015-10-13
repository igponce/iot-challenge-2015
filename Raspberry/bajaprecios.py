"""
bajaprecios.py

Descarga precios de energia desde Azure

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

import urllib.request as ul
import shutil
import sys

from commonconfig import *

resp = ul.urlopen(ENERGY_PRICE_URL)
if resp.code == 200 :
    fp = open(ENERGY_PRICE_FILE, 'wb')
    shutil.copyfileobj(resp, fp)
    fp.close()
else : # aqui pasa something raro
	print("HTTP CODE != 200 - hay que investigar que ocurre")

print(
	"---------------------------------------------------------\n"
	"Precios de energia descargados de Azure                  \n"
	"---------------------------------------------------------\n"
	"Para que este proceso funcione correctamente se debe     \n"
	"ejecutar periodicamente (por ejemplo con este crontab):  \n"
	"0 35 * * *  {}                                           \n"
	"---------------------------------------------------------\n"
	.format(sys.argv[0]) 
	)

#EOF#