# scraper.py

PUBLIC_WEB_DIR = '.'

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

data = scrape_PVPC( dt.datetime.now() )
serialized = pickle.dumps( data )

# Voclamos el fichero donde 'algo' como Azure o un webserver lo pueda leer
fp = open( PUBLIC_WEB_DIR + '/schedule.pickle', 'wb')
fp.write( serialized )
fp.close()

