# iot-challenge-2015
Submission to the microsoft azure IOT Challenge

## Control de corriente electrica usando datos de coste

El proyecto consta de dos partes:

- Azure
 - Programa que descarga los precios diarios de la electricidad y los vuelca a un repositorio compartido.

- Raspberry
 - Control de un relé que abre o cierra un circuito eléctrico en función de:
  - Programación
  - Coste de la electricidad obtenido desde azure
