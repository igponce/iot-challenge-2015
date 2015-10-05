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
import subprocess
import http.server
import urllib.parse

DEFAULT_PORT = 8080

class EnergyAppWebserver(http.server.BaseHTTPRequestHandler):

	def lookupMethod(self):
	    print("ASASDASD")
	    attrname = 'handle_' + self.command.upper() + "_" + self.path[1:]
	    print ("self: {} - command: {} - path: {} - attrname: {}".format(self, self.command.upper(), self.path[:1], attrname))
	    
	    return getattr(self, attrname, None).__call__()
 
	# Routing "sencillo" para la aplicacion
	# Todo se hace en los metodos handle_GET/POST_path de la clase
	# En caso de problemas se manda un 404 (deberia ser un 500 ??)
	def do_GET(self):
		try:
			retval = self.lookupMethod()
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(bytes(retval,'UTF-8'))
		except:
		 	self.send_response(404)
		 	self.end_headers()

	def handle_GET_status(self):
		return "{'ok': 'everything works okay' }"


	def handle_GET_cost(self):
		return '{"yyyy-mm-dd": [ 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24] }'

	def handle_GET_index(self):

		return """
		<!DOCTYPE html>
		<html><head><title>Hello Get</title></head>
		<body>
		   <h1>Hello world</h1>
		   <p>Request command was: {}</p>
		   <p>Requestline = {}</p>
		   <p>Path = {} </p>
		   <p>Params: {} </p>
		</body>
		</html>
		""".format(self.command, self.requestline,  self.path, str(dir(self)))


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



