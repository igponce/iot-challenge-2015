# scraper.py

import urllib.request as ul
import shutil
import xlrd


def leeexcelPVPC (filename):

	book = xlrd.open_workbook(filename)
	sheet = book.sheet_by_index(0)

	for i in range(5,25) :
		fecha = sheet.cell(i,0)
		print(fecha)

def scrape_excel (url, filename):
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

scrape_excel( url, filename)
leeexcelPVPC(filename)