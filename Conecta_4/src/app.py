#Aplicacion conecta 4 en python by: Alfonso
import random

class app():
    def __init__(self):
        self.color = ""
        self.gano = False
        self.opcion = 0
        self.fila = 0
        self.columna = 0
        self.turno = "rojo"
        self.tablero = [
    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"]
]
        self.ficha = 0

    def empezar_juego(self):
        self.opciones_de_juego()
        self.mostrar_instrucciones()
        self.mostrar_tablero()
        if self.opcion == 2:
            print("🤖 La máquina está lista para jugar con el color rojo 🔴. ¡Vamos a ver qué jugada elige!")
        while not self.gano:
            if self.opcion == 1:
                self.elegir_jugada_opcion1()
            if self.opcion == 2:
                self.elegir_jugada_opcion2()
            self.ganador()
            self.tablero_lleno()

    def mostrar_instrucciones(self):
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
    def mostrar_tablero(self):
        print(" 0 1 2 3 4 5 6")
        print("-----------------")
        for fila in self.tablero:
            print("|" + "|".join(fila) + "|")
        print("-----------------")
    def elegir_jugada_opcion1(self):
            try:
                print(f"Turno de {self.turno}")
                columna = input("elige una columna del 0-7 en la que desees jugar: ")
                if columna == "salir":
                    self.gano = True
                    return
                columna = int(columna)
                for fila in range(5, -1, -1):
                    if self.tablero[fila][columna] == "⚪":
                        if self.turno == "rojo":
                            self.tablero[fila][columna] = "🔴"
                            self.turno = "amarillo"
                            self.mostrar_tablero()
                            self.fila = fila
                            self.columna = columna
                            self.ficha = self.tablero[self.fila][self.columna]
                            break
                        else:
                            self.tablero[fila][columna] = "🟡"
                            self.turno = "rojo"
                            self.mostrar_tablero()
                            self.fila = fila
                            self.columna = columna
                            self.ficha = self.tablero[self.fila][self.columna]
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

            total += self.contar_fichas_ganador( self.fila,self.columna, df, dc)
            total += self.contar_fichas_ganador(self.fila, self.columna, -df, -dc)

            if total >= 4:
                if self.ficha == "🔴":
                    print("🔴 ¡Felicidades! El jugador ROJO ha ganado con 4 en línea! 🎉")
                    self.gano = True
                    break
                if self.ficha == "🟡":
                    print("🟡 ¡Felicidades! El jugador AMARILLO ha ganado con 4 en línea! 🎉")
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

        return contador
    def tablero_lleno(self):
        if all("⚪" not in fila for fila in self.tablero):
            print("⚠️ ¡Empate! El tablero está lleno y no hay ganador. Buen juego a ambos. 😄")
            self.gano = True
    def opciones_de_juego(self):
        print("""
        🎮🎉 BIENVENIDO A CONECTA 4 🎉🎮
        =====================================
        Selecciona una opción para comenzar:

        1️⃣  Jugar 2 jugadores (🔴 vs 🟡)
        2️⃣  Jugar contra la máquina (🔴 vs 🤖)
        3️⃣  Salir del juego ❌
        =====================================
        """)
        self.opcion = int(input("Seleccione una opcion: "))
    def elegir_jugada_opcion2(self):
        try:
            print(f"Turno de {self.turno}")
            if self.turno == "rojo":
                columna = random.randint(0, 6)
            else:
                columna = input("elige una columna del 0-7 en la que desees jugar: ")
                if columna == "salir":
                    self.gano = True
                    return
                columna = int(columna)
            for fila in range(5, -1, -1):
                if self.tablero[fila][columna] == "⚪":
                    if self.turno == "rojo":
                           self.tablero[fila][columna] = "🔴"
                           self.turno = "amarillo"
                           self.mostrar_tablero()
                           self.fila = fila
                           self.columna = columna
                           self.ficha = self.tablero[self.fila][self.columna]
                           break
                    else:
                           self.tablero[fila][columna] = "🟡"
                           self.turno = "rojo"
                           self.mostrar_tablero()
                           self.fila = fila
                           self.columna = columna
                           self.ficha = self.tablero[self.fila][self.columna]
                           break

        except Exception as e:
            print(f"No valido: {e}")

    def reiniciar_tablero_al_terminar(self):
            if self.gano:
                self.tablero = [
                    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
                    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
                    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
                    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
                    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"],
                    ["⚪", "⚪", "⚪", "⚪", "⚪", "⚪", "⚪"]
                ]
                self.gano = False
    def reinicio_juego(self):
        while not self.volver_jugar:
            volver_jugar = input("¿Quieres volver a jugar? (s/n)")
            if volver_jugar == "n":
                print("🙌 ¡Gracias por jugar a Conecta 4! Esperamos que te hayas divertido."
                      "Vuelve pronto para otra partida. ¡Hasta luego! 👋")
                self.volver_jugar = True
            else:
                self.reiniciar_tablero_al_terminar()
                self.empezar_juego()



