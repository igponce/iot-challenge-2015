setup.sh

echo << EOF

Este script instala automaticamente en  las dependencias
necesarias para procesar los ficheros excel de Red Electrica
y para subir los datos a la CDN de Azure

Funciona indistintamente desde Windows y Linux.

EOF

read

# Dependencias: Azure, Azure-storagem y XLRD (para leer excel)

pip install azure
pip install azure-storage
pip install xlrd