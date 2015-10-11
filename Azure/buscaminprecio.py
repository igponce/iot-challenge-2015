import pickle
from itertools import repeat

fp = open('schedule.pickle', 'rb')
precio = pickle.load(fp)
fp.close()

# Creamos dos listas de precios para cada uno de los intervalos
# costePorHora[tarifa][dia][h_ini][duracion_en_horas] = euros_por_megawatt
# costePorIntervalo[tarifa][dia][duracion_en_horas][h_inicio] = euros_por_megawatt

todos_costes     = [ 0. for x in range(0,12) ]
# costePorHora     = { "2.0.DHA": list( repeat( [] ,24)) }
# costePorDuracion = { "2.0.DHA": list(repeat( [], 24)) }

costePorHora     = { "2.0.DHA": [ [0.] * 24 for i in range(24) ] }
costePorDuracion = { "2.0.DHA": [ [0.] * 24 for i in range(24) ] }

for dia in precio.keys():
	tarifa = precio[dia]["2.0.DHA"]

	costePorDuracion["2.0.DHA"][1] = [ tarifa[hh] for hh in range(0,23) ]

	for hh in range(0,23):
		costePorHora["2.0.DHA"][hh][1] = tarifa[hh]

	for interval in range(0,10):
		todos_costes[interval] = {}

		for hora in range(0, 24-interval):
			acum = tarifa[hora]
			for j in range(hora,hora+interval):
				acum += tarifa[j]
			todos_costes[interval]["{},{}".format(hora,hora+interval)] = acum
			costePorHora["2.0.DHA"][hora][interval] = acum
			costePorDuracion["2.0.DHA"][interval][hora] = acum

# Obtenemos Lista de horas con menos coste para una duracion determinada:
# minCoste[duracion] = ( hora, coste )

minCoste = []
for dur in range(1,10):
	minCoste[dur] = 0




# TODO
#      - Ordenar el array
#      - Devolver un array de estructuras { inicio: x , fin: x, coste } ordenadas de menor a mayor.

import json
print("PRECIOS ENERGIA:")
print( json.dumps(precio, indent=4, sort_keys=True)  )
# print("\n\nSUMA COSTES")
# print( json.dumps(todos_costes, indent=4, sort_keys=True) )
print("\n\nCostePorHoras")
print( json.dumps(costePorHora, indent=4, sort_keys=False))
print("\n\nCostePorDuracion")
print( json.dumps(costePorDuracion, indent=4, sort_keys=False))

print("\n\n\n**********************\n")
print(costePorDuracion)

