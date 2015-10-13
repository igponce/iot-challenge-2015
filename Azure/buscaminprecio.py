"""
buscaminprecio.py

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

MAX_INTERVAL = 9

"""
   buscaMinPrecio (precio)

   Argumentos:
   	   precio[yyyy-mm-dd][tarifa] = [ euros_megawatt ]

   Devuelve:
       Estructura de datos que contiene los precios de energia mas baratos
       por tarifa, e invervalos horarios (0 para la hora actual, 1 para 2 intervalos, etc.00):

	   minCoste ["nombre_tarifa"][intervalos_horarios] = Array {
				"precio"     : float (coste de megawatio/h)
				"tarifa"     : cadena "nombre_tarifa"
				"hora_inicio": int
				"hora_fin"   : int
				"intervalos" : int
			}

"""

def buscaMinPrecio (precio):

	# Creamos dos listas de precios para cada uno de los intervalos
	# costePorHora[tarifa][dia][h_ini][duracion_en_horas] = euros_por_megawatt
	# costePorIntervalo[tarifa][dia][duracion_en_horas][h_inicio] = euros_por_megawatt

	todos_costes     = [ 0. for x in range(0,12) ]

	for dia in precio.keys():

		costePorHora     = { planprecio: [ [float('inf')] * 24 for i in range(24) ] for planprecio in precio[dia].keys() }
		costePorDuracion = { planprecio: [ [float('inf')] * 24 for i in range(24) ] for planprecio in precio[dia].keys() }

		for planprecio in precio[dia].keys():

			tarifa = precio[dia][planprecio]

			for interval in range(0,6):

				todos_costes[interval] = {}
				for hora in range(0, 24-interval):
					acum = tarifa[hora]
					for j in range(hora,hora+interval):
						acum += tarifa[j]
					todos_costes[interval]["{},{}".format(hora,hora+interval)] = acum
					costePorHora[planprecio][hora][interval] = acum
					costePorDuracion[planprecio][interval][hora] = acum

	# Obtenemos Lista de horas con menos coste para una duracion determinada:
	# minCoste[duracion] = ( hora, coste )

	minCoste = { tarifa: [ [] for i in range(0,MAX_INTERVAL) ] for tarifa in costePorDuracion.keys() }
	for dur in range(0,MAX_INTERVAL):
		for tt in costePorDuracion.keys():
			tempCostes = [ { 'precio': costePorDuracion[tt][dur][hh], 'tarifa': tt , 'hora_inicio': hh, 'hora_fin': hh+dur, 'intevalos': dur } for hh in range(0,23) if costePorHora[tt][dur][hh] != float('inf') ]
			minCoste[tt][dur] = sorted( tempCostes, key = lambda v: v['precio'] )

	return minCoste
