import pickle

fp = open('schedule.pickle', 'rb')
precio = pickle.load(fp)
fp.close()
"""
mininterval = []

for dia in precio.keys():
	for tarifa in precio[dia]:
		# Deberia ser 0..23
		for h_ini in range(0,len(precio[dia][tarifa])-1):
			h_end = min(h_ini+4, 23)
			for intervalo in range(h_ini, h_end):
				# agrupamos de 1 a 12 h
				print ("h_ini: {} -> {} (intervalo={} , hend={}, min({},{})={})".format(h_ini, intervalo,intervalo,h_end, h_ini+4, 23, min(h_ini+4, 23)))

"""

# Crear lista de precios para cada uno de los intervalos
# precio[horas_encendido][(h_ini,h_fin)] = euros_por_megawatt

todos_costes = [0 for x in range(0,12)]

for dia in precio.keys():
	tarifa = precio[dia]["2.0.DHA"]
	# Calculamos de 1 a 10 horas
	for interval in range(1,10):
		todos_costes[interval] = {}
		for i in range(0, 24-interval):
			acum = tarifa[i]
			for j in range(i,i+interval):
				acum += tarifa[j]
			todos_costes[interval]["{},{}".format(i,i+interval)] = acum

import json

print("PRECIOS ENERGIA:")

print( json.dumps(precio, indent=4, sort_keys=True)  )

print("\n\nSUMA COSTES")

print( json.dumps(todos_costes, indent=4, sort_keys=True))


print(todos_costes)