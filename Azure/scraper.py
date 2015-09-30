# scraper.py



# Devuelve dictionary con 'yyyy-mm-dd hh:mm:ss' como clave
# Cada entrada contiene un diccionario con la tarifa y el precio del megawatt en Euros.
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
		precio_key = str(datetime.datetime(yyyy,mm,dd,hh, 0, 0))

		try:
			precio.__getitem__(precio_key)
		except KeyError:
			precio[precio_key] ={}

		precio[precio_key][tarifa] = pvpc


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


filename = 'PVPC_DETALLE_DD_20150929'
url = 'http://www.esios.ree.es/Solicitar?fileName=PVPC_DETALLE_DD_20150929&fileType=xls&idioma=es'

# scrape_excel( url, filename)
leeexcelPVPC(filename)