"""
webcontrol.py

Controla los reles conectados a la raspberry desde la web
utilizando el control manual desde un navegador, y/o
la programacion obtenida desde Red Electrica.

Copyright (C) 2013 Iñigo Gonzalez <igponce (at) gmail (dot) something>

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
"""
import sys
import http.server
import picoweb

DEFAULT_PORT = 8080

class EnergyAppWebserver(picoweb.picoWeb):

	def handle_GET_status(self):
		return "{'ok': 'everything works okay' }"

	def handle_GET_cost(self):
		return '{"yyyy-mm-dd": [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] }'


if __name__ == "__main__":
    # get the port
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = DEFAULT_PORT

    print("Iniciando webserver en puerto: {puerto}\n\n".format(puerto=port))
    server_address = ('', port)

    try:
        httpd = http.server.HTTPServer(server_address, EnergyAppWebserver)
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Terminando proceso servidor')
        httpd.socket.close()

