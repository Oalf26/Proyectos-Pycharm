import http.server
import socketserver
import json


# --- Funciones para manejar la base de datos ---
def leer_datos():
    try:
        with open('database.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def escribir_datos(datos):
    with open('database.json', 'w', encoding='utf-8') as f:
        json.dump(datos, f, indent=4)


# --- El manejador de la API ---
class APIHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/mascotas':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            # CORS Header: Permite que el FE (en puerto 8001) hable con el BE (en 8000)
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()

            datos = leer_datos()
            self.wfile.write(json.dumps(datos).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Ruta no encontrada')


# --- El código que arranca el servidor ---
PORT = 8000
with socketserver.TCPServer(("", PORT), APIHandler) as httpd:
    print("Servidor escuchando en el puerto", PORT)
    httpd.serve_forever()