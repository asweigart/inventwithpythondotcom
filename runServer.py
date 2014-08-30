#! python3

# Runs a simple web server on the output folder.

import os
import http.server

os.chdir('output') # this is meant to be run from the project root folder

# This code is mostly copied from the Python standard library code.

http.server.SimpleHTTPRequestHandler.protocol_version = 'HTTP/1.0'
httpd = http.server.HTTPServer(('', 8000), http.server.SimpleHTTPRequestHandler)

sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nKeyboard interrupt received, exiting.")
    httpd.server_close()
