class Game:
    def __init__(self):
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
    def mostrar_tablero(self):
        print(" 0 1 2 3 4 5 6")
        print("-----------------")
        for fila in self.tablero:
            print("|" + "|".join(fila) + "|")
        print("-----------------")
    def colocar_ficha(self, columna, turno):
     try:
        print(f"Turno de {turno}")
        for fila in range(5, -1, -1):
            if self.tablero[fila][columna] == "⚪":
                if turno == "rojo":
                    self.tablero[fila][columna] = "🔴"
                    turno = "amarillo"
                    self.mostrar_tablero()
                    self.ficha = self.tablero[fila][columna]
                    self.fila = fila
                    self.columna = columna
                    break
                else:
                    self.tablero[fila][columna] = "🟡"
                    turno = "rojo"
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
                    self.gano = True
                    break
                if self.ficha == "🟡":
                    self.gano = True
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
            self.gano = True
class Player:
    def __init__(self):
    def elegir_columna(self):
        columna = input("elige una columna del 0-7 en la que desees jugar: ")
        return columna
class humanPlayer:
    pass
class IA:
    pass
class menssajes:
    pass
class instruction:
    pass