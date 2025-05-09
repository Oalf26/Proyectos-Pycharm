import random
class Game:
    def __init__(self):
        self.turno = "rojo"
        self.tablero = Board()
        self.jugador = Player()
        self.mensajes = menssajes()
        self.instrucciones = instruction()
    def empezar_juego(self, opcion, tipo):
        if opcion == 1:
            while not self.gano:
              self.tablero.mostrar_tablero()
              self.jugador = Player(tipo, self.turno)
              columna = self.jugador.elegir_columna()
              if columna == "salir":
                  break
              self.tablero.colocar_ficha(columna)
              self.cambiar_turno()
              self.tablero.ganador()
              self.tablero.tablero_lleno()

    def cambiar_turno(self):
        if self.turno == "rojo":
            self.turno = "amarillo"
        else:
            self.turno = "rojo"
    def gano(self, boleano):
            gano = boleano
            return gano
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
                    Game.gano(self, True)
                    break
                if self.ficha == "🟡":
                    Game.gano(self, True)
                    break
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
    def tablero_lleno(self):
        if all("⚪" not in fila for fila in self.tablero):
            print("⚠️ ¡Empate! El tablero está lleno y no hay ganador. Buen juego a ambos. 😄")
            Game.gano(self, True)

class Player:
    def __init__(self, tipo, turno):
        self.tipo = tipo
        self.turno = turno
    def elegir_columna(self):
        if self.tipo == "human":
            print(f"Turno de {self.turno}")
            columna = input("elige una columna del 0-7 en la que desees jugar: ")
            if columna == "salir":
                return "salir"
            return int(columna)
        elif self.tipo == "maquina" and self.turno == "rojo":
            return random.randint(0, 6)
class menssajes:
    pass
class instruction:
    pass