#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


# Création d'une classe qui gère les requêtes HTTP
class SimpleAPIHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Gère les requêtes GET selon le chemin demandé"""

        # Route principale "/"
        if self.path == "/":
            self.send_response(200)  # Code de succès HTTP
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")  # Réponse texte

        # Endpoint "/data" → renvoie un JSON
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        # Endpoint "/status" → renvoie "OK"
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            status = {"status": "OK"}
            self.wfile.write(json.dumps(status).encode())

        # Endpoint "/info" → renvoie informations sur l’API
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode())

        # Si l’endpoint n’existe pas → 404
        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode())


# Configuration du serveur
def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    server_address = ('', 8000)  # Serveur sur le port 8000
    httpd = server_class(server_address, handler_class)
    print("Server running at http://localhost:8000")
    httpd.serve_forever()  # Le serveur tourne en continu


# Point d’entrée du script
if __name__ == "__main__":
    run()
