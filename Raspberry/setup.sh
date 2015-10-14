#!//bin/bash 
# setup.sh

cat << EOF

Este script instala automaticamente en la raspberry las dependencias
necesarias para controlar los relés a través de los puertos GPIO
y para hablar con el servidor de AZURE.

Necesita privilegios de root (!!!)

Pulsa enter para instalar....

EOF

read

sudo apt-get install python-dev python-rpi.gpio
