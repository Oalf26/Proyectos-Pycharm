import tkinter as tk
import utils
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.turno = "roja"
        self.tablero = [[None for _ in range(6)] for _ in range(7)]
        self.ventana()
        self.crear_tablero()
    def ventana(self):
        self.title("Conecta 4")
        self.configure(bg="#1E1E1E")
        self.attributes("-alpha", 0.96)
        w, h = 700, 500
        utils.centrar_ventana(self, h, w)
    def crear_tablero(self):
        CELDA = 80
        VENTANA_ANCHO = 560
        VENTANA_ALTO = 440
        self.canva = tk.Canvas(self, width=VENTANA_ANCHO, height=VENTANA_ALTO, bg="blue")
        self.canva.pack()

        for x in range(7):
            for y in range(6):
                x1 = x * CELDA
                y1 = y * CELDA
                x2 = x1 + CELDA
                y2 = y1 + CELDA
                self.canva.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill="white", outline="black")
        self.canva.bind("<Button-1>", self.al_click)
    def al_click(self, event):
            columna = event.x // 80
            self.colocar_ficha(columna)
    def colocar_ficha(self, columna):
        for fila in range(5, -1, -1):
            if self.tablero[columna][fila] is None:
                x1 = columna * 80
                y1 = fila * 80
                x2 = x1 + 80
                y2 = y1 + 80

                color_ficha = "red" if self.turno == "roja" else "yellow"
                self.canva.create_oval(x1 + 5, y1 + 5, x2 - 5, y2 - 5, fill=color_ficha, outline="black")
                self.tablero[columna][fila] = self.turno
                self.turno = "amarilla" if self.turno == "roja" else "roja"
                break







