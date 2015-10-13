setup.sh

echo << EOF

Este script instala automaticamente en la raspberry las dependencias
necesarias para controlar los relés a través de los puertos GPIO
y para hablar con el servidor de AZURE.

Necesita privilegios de root (!!!)

EOF

read

# Dependencias: Azure, Azure-storagem y XLRD (para leer excel)

pip install azure
pip install azure-storage
pip install xlrd