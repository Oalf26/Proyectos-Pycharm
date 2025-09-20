import http.server
import json
import socketserver
from http.server import (SimpleHTTPRequestHandler)
import urllib.parse as par

def Data():
        with open("database_practica.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
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
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/ping':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Pong")
        elif self.path == '/Carros' + "?" + path.query:
            try:
                data = Data()
                self.send_response(200)
            except (json.JSONDecodeError, FileNotFoundError) as e:
                self.send_response(500)
                data = {"error": "Problema con la base de datos: " + str(e)}
            self.send_header("Content-type", "application/json")
            self.end_headers()
            for item in data:
                if brand == item["brand"]:
                    self.wfile.write(json.dumps(item["models"]).encode('utf-8'))
                else:
                    self.wfile.write(b"Modelo no existente")
                    break
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Ruta no encontrada")
    def do_POST(self):
        if self.path == "/Carros":
            try:
                longitud = int(self.headers["Content-Length"])
                body = self.rfile.read(longitud)
                data = body.decode("utf-8")
                data = json.loads(data)
                add(data)
                self.send_response(201)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"Mensaje": "Informacion recibida"}).encode("utf-8"))
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
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Ruta no encontrada")
PORT = 8000
with socketserver.TCPServer(("", PORT), Myhandler) as httpd:
    print("Escuchando en el puerto" , PORT)
    httpd.serve_forever()
#postman
#Como mandar desde la url que tengo aqui un parametro por el metodo get hacia el backend
#http://localhost:8080/carros?brand=Toyota
#Modificar la función handle para que por el metodo get pueda recibir el parametro marca = brand
#Este metodo debe ser por GET, el cual va a buscar la marca en base de datos y va a retornar el modelo de esa marca que le estas enviando.
#Estudiar los metodos de comunicación http para comunicarse con servios REST
#investigar como leer el json para mostrar el modelo de la marca que estas buscando.
#ver un tutorial de como usar postman: como probar un get y post