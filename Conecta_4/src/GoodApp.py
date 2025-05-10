import random
class Game:
    def __init__(self):
        self.gano = False
        self.tipo = 0
        self.turno = "rojo"
        self.tablero = Board()
        self.jugador = Player(self.tipo, self.turno)
        self.mensajes = menssajes()
        self.instrucciones = instruction()
    def empezar_juego(self):
        opcion = self.mensajes.opciones()
        self.instrucciones.instrucciones()
        self.tablero.mostrar_tablero()
        while not self.gano:
                if opcion == 1:
                    self.tipo = "human"
                if opcion == 2:
                    self.tipo = "maquina"
                self.jugador = Player(self.tipo, self.turno)
                columna = self.jugador.elegir_columna()
                if columna == "salir":
                    self.gano = True
                self.tablero.colocar_ficha(columna)
                self.cambiar_turno()
                self.tablero.ganador()
                if self.tablero.ganador():
                    self.gano = True
                if self.tablero.tablero_lleno():
                    self.mensajes.empate()
                    self.gano = True

    def cambiar_turno(self):
        if self.turno == "rojo":
            self.turno = "amarillo"
        else:
            self.turno = "rojo"
class Board:
    def __init__(self):
        self.tablero = [
            ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
            ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
            ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
            ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
            ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
            ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"]
        ]
        self.ficha = 0
        self.fila = 0
        self.columna = 0
        self.turno = "rojo"
        self.mensajes = menssajes()
    def mostrar_tablero(self):
        print(" 0 1 2 3 4 5 6")
        print("-----------------")
        for fila in self.tablero:
            print("|" + "|".join(fila) + "|")
        print("-----------------")
    def colocar_ficha(self, columna):
     try:
        for fila in range(5, -1, -1):
            if self.tablero[fila][columna] == "⚪":
                if self.turno == "rojo":
                    self.tablero[fila][columna] = "🔴"
                    self.turno = "amarillo"
                    self.mostrar_tablero()
                    self.ficha = self.tablero[fila][columna]
                    self.fila = fila
                    self.columna = columna
                    break
                else:
                    self.tablero[fila][columna] = "🟡"
                    self.turno = "rojo"
                    self.mostrar_tablero()
                    self.ficha = self.tablero[fila][columna]
                    self.fila = fila
                    self.columna = columna
                    break

     except Exception as e:
       print(f"No valido: {e}")
    def ganador(self):
        direcciones = [
            (0, 1),  # Horizontal →
            (1, 0),  # Vertical ↓
            (1, 1),  # Diagonal ↘︎
            (1, -1),  # Diagonal ↙︎
        ]
        for df, dc in direcciones:
            total = 1

            total += self.contar_fichas_ganador(self.fila, self.columna, df, dc)
            total += self.contar_fichas_ganador(self.fila, self.columna, -df, -dc)

            if total >= 4:
                if self.ficha == "🔴":
                    self.mensajes.gana_rojo()
                    return True
                if self.ficha == "🟡":
                    self.mensajes.gana_amarillo()
                    return True
    def contar_fichas_ganador(self,fila, columna, direccion_fila, direccion_columna):
        contador = 0
        for i in range(1, 4):
            f = fila + direccion_fila * i
            c = columna + direccion_columna * i
            if 0 <= f < 6 and 0 <= c < 7:
                if self.tablero[f][c] == self.ficha:
                    contador += 1
                else:
                    break
            else:
                break
        return contador
    def tablero_lleno(self):
        if all("⚪" not in fila for fila in self.tablero):
            return True

class Player:
    def __init__(self, tipo, turno):
        self.tipo = tipo
        self.turno = turno
    def elegir_columna(self):
        print(f"Turno de {self.turno}")
        if self.tipo == "human":
            columna = input("elige una columna del 0-7 en la que desees jugar: ")
            if columna == "salir":
                return "salir"
            return int(columna)
        elif self.tipo == "maquina" and self.turno == "rojo":
            return random.randint(0, 6)
        else:
            columna = input("elige una columna del 0-7 en la que desees jugar: ")
            if columna == "salir":
                return "salir"
            return int(columna)
class menssajes:
    def gana_rojo(self):
        print("🔴 ¡Felicidades! El jugador ROJO ha ganado con 4 en línea! 🎉")
    def gana_amarillo(self):
        print("🟡 ¡Felicidades! El jugador AMARILLO ha ganado con 4 en línea! 🎉")
    def empate(self):
        print("⚠️ ¡Empate! El tablero está lleno y no hay ganador. Buen juego a ambos. 😄")
    def opciones(self):
        print("""
                🎮🎉 BIENVENIDO A CONECTA 4 🎉🎮
                =====================================
                Selecciona una opción para comenzar:

                1️⃣  Jugar 2 jugadores (🔴 vs 🟡)
                2️⃣  Jugar contra la máquina (🔴 vs 🤖)
                3️⃣  Salir del juego ❌
                =====================================
                """)
        opcion = int(input("Seleccione una opcion: "))
        return opcion
class instruction:
    def instrucciones(self):
        print("""
                   Bienvenido al juego Conecta 4! 🎮

                   Instrucciones:
                   1. El tablero tiene 6 filas y 7 columnas.
                   2. Dos jugadores se turnan para colocar una ficha en una de las 7 columnas.
                   3. La ficha caerá en la fila más baja disponible de la columna seleccionada.
                   4. El objetivo es alinear 4 fichas del mismo color de forma vertical, horizontal o diagonal.
                   5. El jugador con 4 fichas alineadas gana el juego.
                   6. El jugador rojo usa 🔴 y el jugador amarillo usa 🟡.
                   7. Escriba "salir" si desea salir

                   ¡Que empiece el juego! 😄
                   """)