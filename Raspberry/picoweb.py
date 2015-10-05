"""
picoweb.py

Picoweb "framework"
Simple, stupid, way of handling HTTP requests from a class
with fallback to static content (in the /static directory).

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
import subprocess
import http.server
import urllib.parse

DEFAULT_PORT = 8080

class picoWeb (http.server.BaseHTTPRequestHandler):

	"""
	    processMethod
	    --------------
	    Ejecutamos el metodo de la clase solicitado por la aplicacion a traves del path.
	    Si no disponemos del metodo, volcamos el contenido del fichero que
	    coincide con el path dentro del directorio 'static'.

	"""
	def processMethod(self):

	    attrname = 'handle_' + self.command.upper() + "_" + self.path[1:]
	    retval = ''

	    try:
	    	retval = getattr(self, attrname, None).__call__()
	    	return retval

	    except :
		    fp = open ('static' + self.path )
		    retval = fp.read()
		    fp.close()
		    return retval
 
	# Routing "sencillo" para la aplicacion
	# Todo se hace en los metodos handle_GET/POST_path de la clase
	# En caso de problemas se manda un 404 (deberia ser un 500 ??)

	def do_GET(self):
		try:
			content = self.processMethod()
			self.send_response(200)
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(bytes(content,'UTF-8'))
		except:
		 	self.send_response(404)
		 	self.end_headers()


if __name__ == "__main__":
    # get the port
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = DEFAULT_PORT

    print("Starting webserver @port: {puerto}\n\n".format(puerto=port))
    server_address = ('', port)

    try:
        httpd = http.server.HTTPServer(server_address, picoWeb)
        httpd.serve_forever()

    except KeyboardInterrupt:
        print('Terminando proceso servidor')
        httpd.socket.close()

