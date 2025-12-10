import http.server
import json
import socketserver
from http.server import (SimpleHTTPRequestHandler)
import urllib.parse as par

def Data():
        with open("database_practica.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
def delete(item):
    data = Data()
    data.pop(item)
    with open("database_practica.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def add(body):
    data = Data()
    data.append(body)
    with open("database_practica.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
def query_string(url):
    query = par.urlparse(url)
    query = par.parse_qs(query.query)
    brand = query.get("brand", [None])[0]
    return brand


class Myhandler(SimpleHTTPRequestHandler):
    def http_headers(self):
        self.send_header("Content-type", "application/json")
        self.end_headers()
    def write(self, message):
        self.wfile.write(message)
    def http_header_404(self):
        self.send_response(404)
        self.end_headers()
    def add_information(self, information):
        body = self.rfile.read(information)
        data = body.decode("utf-8")
        data = json.loads(data)
        return data

    def do_GET(self):
        brand = query_string(self.path)
        path = par.urlparse(self.path)
        if self.path == '/Carros':
            try:
                data = Data()
                self.send_response(200)
            except (json.JSONDecodeError, FileNotFoundError) as e:
                self.send_response(500)
                data = {"error": "Problema con la base de datos: " + str(e)}
            self.http_headers()
            self.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/ping':
            self.send_response(200)
            self.end_headers()
            self.write(b"Pong")
        elif self.path == '/Carros' + "?" + path.query:
            try:
                data = Data()
                self.send_response(200)
            except (json.JSONDecodeError, FileNotFoundError) as e:
                self.send_response(500)
                data = {"error": "Problema con la base de datos: " + str(e)}
            self.http_headers()
            for item in data:
                if brand == item["brand"]:
                    self.write(json.dumps(item["models"]).encode('utf-8'))
                    break
                else:
                    self.write(b"Modelo no existente")

        else:
            self.http_header_404()
            self.write(b"Ruta no encontrada")
    def do_POST(self):
        if self.path == "/Carros":
            try:
                longitud = int(self.headers["Content-Length"])
                data = self.add_information(longitud)
                add(data)
                self.send_response(201)
                self.http_headers()
                self.write(json.dumps({"Mensaje": "Informacion recibida"}).encode("utf-8"))
            except json.JSONDecodeError:
                self.send_response(400)
                self.http_headers()
                self.write(json.dumps({"error": "JSON invalido"}).encode("utf-8"))

            except Exception as e:
                self.send_response(500)
                self.http_headers()
                self.write(json.dumps({"error": "Problema con la base de datos: " + str(e)}).encode("utf-8"))
        else:
            self.http_header_404()
            self.write(b"Ruta no encontrada")
    def do_DELETE(self):
        brand = query_string(self.path)
        path = par.urlparse(self.path)
        if self.path == '/Carrosdelete' + "/brand" + "?" + path.query:
                try:
                    data = Data()
                    self.send_response(201)
                except json.JSONDecodeError:
                    self.send_response(400)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "JSON invalido"}).encode("utf-8"))
                except Exception as e:
                    self.send_response(500)
                    self.send_header("Content-type", "application/json")
                    self.end_headers()
                    self.wfile.write(json.dumps({"error": "Problema con la base de datos: " + str(e)}).encode("utf-8"))
                self.http_headers()
                for item in data:
                    if brand == item["brand"]:
                        delete(item)
                        self.write(json.dumps({"Mensaje": "Se ha eliminado con exito la marca:" + brand}).encode("utf-8"))
                        break
                    else:
                        self.write(b"Modelo no existente")

        else:
            self.send_response(404)
            self.end_headers()
            self.write(b"Ruta no encontrada")
PORT = 8000
with socketserver.TCPServer(("", PORT), Myhandler) as httpd:
    print("Escuchando en el puerto" , PORT)
    httpd.serve_forever()

#Aprender significados de los codigos http
#Identificar codigo reperido en mi codigo actual
#Crear funciones para evitar repetir codigo e identificar variables