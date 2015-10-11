"""
scraper.py

Obtiene el fichero excel de precios de la energia de Red Electrica
y lo trata para calcular los costes de uso de energia en distintos intervalos horarios.
(2,3,4 horas seguidas, etc.)

Salida:
	- Fichero .json que contiene esta estructura de datos:

		precio["nombre_tarifa"][intervalo_horas] = Array {
			coste: float (coste de megawatio/h)
			"hora_inicio": int
			"hora_fin": int
		}

		El contenido del array está ordenado de menor a mayor coste.
		Es decir:

			precio["2.0.DHA"][4][0] <- Contiene la hora inicio y final de menor coste.
			precio["2.0.DHA"][4][1] <- Contiene la hora de incio y final con el segundo menor coste.

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

PUBLIC_WEB_DIR = '.'
OUTPUT_FILENAME = "precios.json"

# Devuelve dictionary con 'yyyy-mm-dd hh:mm:ss' como clave
# Cada entrada contiene un diccionario con la tarifa y el precio del megawatt en Euros:
# precio[yyyy-mm-dd][tarifa] = euros_megawatt
	
def leeexcelPVPC (filename):

	import xlrd
	import datetime

	book = xlrd.open_workbook(filename)
	sheet = book.sheet_by_index(0)

	precio = {}

	for i in range(5,77) :
		(yyyy, mm, dd, hh, mi, ss) = xlrd.xldate_as_tuple( sheet.cell_value(i,0), book.datemode )
		fecha  = (yyyy, mm, dd, hh, mi, ss)	
		hh     = int( sheet.cell_value(i,1) ) - 1 # Hora del precio
		tarifa = sheet.cell_value(i,2)
		tramo  = int( sheet.cell_value(i,3) )
		pvpc   = sheet.cell_value(i,4)
		precio_key = "{}-{}-{}".format(yyyy,mm,dd)

		try:
			precio.__getitem__(precio_key)
		except KeyError:
			precio[precio_key] = {}

		try:
			precio[precio_key].__getitem__(tarifa)
		except KeyError:
			precio[precio_key][tarifa] = []

		precio[precio_key][tarifa].insert(i-5, pvpc)

	return precio

def scrape_excel (url, filename):
	
	import urllib.request as ul
	import shutil

	retval = False
	resp = ul.urlopen(url)
	if resp.code == 200 :
	    fp = open(filename, 'wb')
	    shutil.copyfileobj(resp, fp)
	    fp.close()
	    retval = True

	return retval

def scrape_PVPC (tiempo):

	filename = "PVPC_DETALLE_DD_{:%Y%m%d}".format(tiempo)
	url = "http://www.esios.ree.es/Solicitar?fileName={}&fileType=xls&idioma=es".format(filename)
	scrape_excel(url, filename)
	return leeexcelPVPC(filename)

import datetime as dt
import pickle

#data = scrape_PVPC( dt.datetime.now() )
serialized = pickle.dumps( data )

# Voclamos el fichero donde 'algo' como Azure o un webserver lo pueda leer
fp = open( PUBLIC_WEB_DIR + '/schedule.pickle', 'wb')
fp.write( serialized )
fp.close()

