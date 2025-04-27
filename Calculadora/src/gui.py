import tkinter as tk
import tkinter.font as font
import config
import utils
import cientifica
import math
import re
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.cientifico_activo = False
        self.ventana()
        self.construir_widget()
        for i in range(8):
            self.grid_columnconfigure(i, weight=1)
        for i in range(10):
            self.grid_rowconfigure(i, weight=1)

    def ventana(self):
        self.title("Calculadora")
        self.configure(bg=config.COLOR_FONDO)
        self.attributes("-alpha", 0.96)
        w, h = 500, 700
        utils.centrar_ventana(self, h, w)

    def construir_widget(self):
        self.boton_menu = tk.Button(self, text="☰", font=("Arial", 14), bg=config.COLOR_BOTON,
                                    fg=config.COLOR_TEXTO, bd=0, command= self.abrir_operaciones_cientificas)
        self.boton_menu.grid(row=0, column=0, sticky="W", padx=10, pady=5)
        self.etiqueta_operacion_hecha = tk.Label(self, text="", font=(
            "Fira Code", 16, "normal"), fg= config.COLOR_TEXTO , bg= config.COLOR_FONDO, justify='right'
        )
        self.etiqueta_operacion_hecha.grid(row=0, column=3,sticky="nsew",columnspan=8, padx= 10 , pady= 10)

        self.pantalla_operacion=tk.Entry(self, width=12, font=(
            "Fira Code", 32, "bold"),bd=0, fg=config.COLOR_TEXTO , bg=config.COLOR_FONDO, justify='right')
        self.pantalla_operacion.grid(row=1, column=0,columnspan= 8,sticky="nsew",  padx=10, pady=10)

        botones = [
            "DEL", "AC", "%", "÷",
            "7", "8", "9", "x",
            "4", "5", "6", "-",
            "1", "2", "3", "+",
            "0", ".", "="
        ]

        row_val = 2
        col_val = 0

        for boton in botones:
            if boton in ["DEL", "AC","%", "÷", "x", "-",
                         "+","=", "."]:
                color_fondo = config.COLOR_BOTON_OPERACION
                boton_font = font.Font(family="JetBrains Mono", size=20, weight="bold")

            else:
                color_fondo = config.COLOR_BOTON
                boton_font = config.FUENTE_BOTONES

            if boton == "=":
                tk.Button(self, text=boton, width= 11, height= 2,command = lambda b=boton: self.funcion_botones(b),
                          bg=color_fondo, fg=config.COLOR_TEXTO, relief=tk.FLAT, font=boton_font,  padx=5, pady=5, bd=0,
                          borderwidth=0, highlightthickness=0,
                          overrelief='flat').grid(row=row_val, column=col_val,sticky="nsew", columnspan=2 , pady=5)
            else:
                 tk.Button(self, text = boton, width= 5, height= 2, command = lambda b=boton: self.funcion_botones(b),
                           bg= color_fondo, fg=config.COLOR_TEXTO, relief=tk.FLAT, font= boton_font, padx=5, pady=5, bd= 0, borderwidth=0, highlightthickness= 0,
                           overrelief= 'flat').grid(row=row_val, sticky="nsew", column=col_val, pady=5, padx =5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        self.frame_cientifico = tk.Frame(self, bg=config.COLOR_FONDO)
        self.frame_cientifico.grid(row=2, column=4, rowspan=5, padx=10, pady=5)
        self.frame_cientifico.grid_remove()
        operaciones_cientificas = ["sin(", "cos(", "tan(", "asin(", "acos(", "atan(",
                                 "log(","ln(","abs(", "round(", "floor(", "ceil(",
                                  "factorial(","pi", "e", "^", "exp(","sqrt(",
                                 ]

        fila = 0
        col = 0

        for ope in operaciones_cientificas:
            tk.Button(self.frame_cientifico, text=ope, width= 6, height= 2,
                              command=lambda o=ope: self.funcion_botones(o),
                              bg=config.COLOR_BOTON_CIENTIFICO, fg=config.COLOR_TEXTO,
                              relief=tk.FLAT, font=config.FUENTE_BOTONES, padx=5, pady=5, bd=0).grid(row=fila, column=col,sticky="nsew", padx=5, pady=5)
            fila += 1
            if fila > 4:
                fila = 0
                col += 1

    def funcion_botones(self, value):
        if value == "=":
            try:
                expression = self.pantalla_operacion.get().replace("x", "*").replace("÷", "/").replace("%", "/100")
                result = cientifica.evaluar_expresion(expression)
                self.pantalla_operacion.delete(0, tk.END)
                self.pantalla_operacion.insert(tk.END, str(result))
                operation = expression + "" + value
                self.etiqueta_operacion_hecha.config(text=operation)
            except Exception as e:
                self.pantalla_operacion.delete(0, tk.END)
                self.pantalla_operacion.insert(tk.END, "Error b ")
                self.etiqueta_operacion_hecha.config(text="")
        elif value == "AC":
            self.pantalla_operacion.delete(0, tk.END)
            self.etiqueta_operacion_hecha.config(text="")
        elif value == "DEL":
            texto_actual = self.pantalla_operacion.get()
            if texto_actual:
                nuevo_texto = texto_actual[:-1]
                self.pantalla_operacion.delete(0, tk.END)
                self.pantalla_operacion.insert(0, nuevo_texto)
        elif value in ["sin(", "cos(", "tan(", "asin(", "acos(", "atan(", "log(", "ln(", "abs(", "round(", "floor(",
                       "ceil(", "factorial(", "sqrt(", "exp("]:
            self.pantalla_operacion.insert(tk.END, value)
        elif value in ["pi", "e"]:
            self.pantalla_operacion.insert(tk.END, value)
        elif value == "^":
            self.pantalla_operacion.insert(tk.END, "^")
        else:
           texto_actual = self.pantalla_operacion.get()
           self.pantalla_operacion.delete(0, tk.END)
           self.pantalla_operacion.insert(tk.END, texto_actual + value)
           if value == "=":
               self.pantalla_operacion.config(text="")

    def abrir_operaciones_cientificas(self):
       if self.cientifico_activo:
           self.frame_cientifico.grid_remove()
           self.geometry("400x650")
           self.cientifico_activo = False
       else:
            self.frame_cientifico.grid()
            self.geometry("900x1400")
            self.cientifico_activo = True






