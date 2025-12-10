import random


class Game:
    def __init__(self):
        self.gano = False
        self.tipo = 0
        self.turno = "rojo"
        self.tablero = Board()
        self.jugador = Player(self.tipo, self.turno)
        self.mensajes = Mensajes()
        self.instrucciones = Instruction()

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
            else:
                self.tablero.colocar_ficha(columna, self.turno)
                if self.tablero.ganador():
                    self.gano = True
                elif self.tablero.tablero_lleno():
                    self.mensajes.empate()
                    self.gano = True
                else:
                    self.cambiar_turno()

    def cambiar_turno(self):
        self.turno = "amarillo" if self.turno == "rojo" else "rojo"
        return self.turno


class Board:
    def __init__(self):
        self.tablero = [["⚪"] * 7 for _ in range(6)]
        self.ficha = 0
        self.fila = 0
        self.columna = 0
        self.mensajes = Mensajes()

    def reiniciar_tablero(self):
        self.tablero = [["⚪"] * 7 for _ in range(6)]
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
            for fila in range(5, -1, -1):
                if self.tablero[fila][columna] == "⚪":
                    self.ficha = "🔴" if turno == "rojo" else "🟡"
                    self.tablero[fila][columna] = self.ficha
                    self.fila = fila
                    self.columna = columna
                    self.mostrar_tablero()
                    break
        except Exception as e:
            print(f"No válido: {e}")

    def ganador(self):
        direcciones = [(0, 1), (1, 0), (1, 1), (1, -1)]
        for df, dc in direcciones:
            total = 1
            total += self.contar_fichas_ganador(self.fila, self.columna, df, dc)
            total += self.contar_fichas_ganador(self.fila, self.columna, -df, -dc)
            if total >= 4:
                if self.ficha == "🔴":
                    self.mensajes.gana_rojo()
                else:
                    self.mensajes.gana_amarillo()
                self.reiniciar_tablero()
                return True
        return False

    def contar_fichas_ganador(self, fila, columna, df, dc):
        contador = 0
        for i in range(1, 4):
            f = fila + df * i
            c = columna + dc * i
            if 0 <= f < 6 and 0 <= c < 7 and self.tablero[f][c] == self.ficha:
                contador += 1
            else:
                break
        return contador

    def tablero_lleno(self):
        if all("⚪" not in fila for fila in self.tablero):
            self.reiniciar_tablero()
            return True
        return False


class Player:
    def __init__(self, tipo, turno):
        self.tipo = tipo
        self.turno = turno

    def elegir_columna(self):
        print(f"Turno de {self.turno}")
        if self.tipo == "human":
            columna = input("Elige una columna del 0-6 en la que desees jugar: ")
            if columna == "salir":
                return "salir"
            return int(columna)
        elif self.tipo == "maquina" and self.turno == "rojo":
            return random.randint(0, 6)
        else:
            columna = input("Elige una columna del 0-6 en la que desees jugar: ")
            if columna == "salir":
                return "salir"
            return int(columna)


class Mensajes:
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
        opcion = int(input("Seleccione una opción: "))
        return opcion

    def gracias_por_jugar(self):
        print("🙌 ¡Gracias por jugar a Conecta 4! Esperamos que te hayas divertido. "
              "Vuelve pronto para otra partida. ¡Hasta luego! 👋")

    def volver_jugar(self):
        return input("¿Quieres volver a jugar? (s/n): ")


class Instruction:
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


class GameAgain:
    def __init__(self):
        self.termino = False
        self.mensajes = Mensajes()
        self.juego = Game()

    def volver_jugar(self):
        while not self.termino:
            respuesta = self.mensajes.volver_jugar()
            if respuesta.lower() == "n":
                self.mensajes.gracias_por_jugar()
                self.termino = True
            else:
                self.juego.empezar_juego()
