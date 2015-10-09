"""
webcontrol.py

Controla los reles conectados a la raspberry desde la web
utilizando el control manual desde un navegador, y/o
la programacion obtenida desde Red Electrica.

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

import sys
import http.server
import json
import picoweb

DEFAULT_PORT = 8080
FICHERO_DATOS = '../Azure/schedule.pickle'

precios = {}
estado = { "planificado": False, 'powerStart': 0, 'powerEnd': 0 }
config = { "tarifa": "2.0DHA ", "powerTime": 0 }

def cargaDatos (fichero):
    import pickle
    fp = open (FICHERO_DATOS, 'rb')
    serialized = fp.read()
    precios = pickle.loads( serialized )
    fp.close()
    return precios

class EnergyAppWebserver(picoweb.picoWeb):

    # Obtencion de datos
    def handle_GET_status(self):
        return json.dumps(estado, indent=4)

    def handle_GET_config(self):
        return json.dumps(config, indent=4)

    def handle_GET_precios(self):
        return json.dumps(precios, sort_keys=True, indent=4)

    def handle_POST_programar(self):
        return json.dumps("")


if __name__ == "__main__":

    # if len(sys.argv) > 1
    #     port = int(sys.argv[1])
    # else:
    port = DEFAULT_PORT

    precios = cargaDatos(FICHERO_DATOS)
    print("Iniciando webserver en puerto: {puerto}\n\n".format(puerto=port))
    server_address = ('', port)

    try:
        httpd = http.server.HTTPServer(server_address, EnergyAppWebserver)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Terminando proceso servidor')
        httpd.socket.close()

