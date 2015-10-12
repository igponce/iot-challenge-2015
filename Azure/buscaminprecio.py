import pickle
from itertools import repeat
import pprint

MAX_INTERVAL = 9

fp = open('schedule.pickle', 'rb')
precio = pickle.load(fp)
fp.close()

# Creamos dos listas de precios para cada uno de los intervalos
# costePorHora[tarifa][dia][h_ini][duracion_en_horas] = euros_por_megawatt
# costePorIntervalo[tarifa][dia][duracion_en_horas][h_inicio] = euros_por_megawatt

todos_costes     = [ 0. for x in range(0,12) ]
# costePorHora     = { "2.0.DHA": list( repeat( [] ,24)) }
# costePorDuracion = { "2.0.DHA": list(repeat( [], 24)) }

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
		tempCostes = [ { 'precio': costePorDuracion[tt][dur][hh], 'tarifa': tt , 'hora_inicio': hh, 'hora_fin': hh+dur 'intevalos': dur } for hh in range(0,23) if costePorHora[tt][dur][hh] != float('inf') ]
		minCoste[tt][dur] = sorted( tempCostes, key = lambda v: v['precio'] )


# TODO
#      - Ordenar el array
#      - Devolver un array de estructuras { inicio: x , fin: x, coste } ordenadas de menor a mayor.

import json
print("PRECIOS ENERGIA:")
pprint.pprint( json.dumps(precio, indent=4, sort_keys=True)  )

print("\n\nSUMA COSTES")
pprint.pprint( todos_costes )

print("Precios minimos por duracion")
pprint.pprint(minCoste)
