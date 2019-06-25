#coding:UTF-8
import http.server


# Serveur http de base delivrant le contenu du repertoire courant via le port indique.
port = 9080
adress = ("", port)
server = http.server.HTTPServer

# Python 3 // CGI :
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/cgi-bin"]

httpd = server(adress, handler)
print("à l'écoute sur le port :", port)
httpd.serve_forever()