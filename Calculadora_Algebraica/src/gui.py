import sympy
import utils
import tkinter as tk
import logic
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.grid_columnconfigure(0, weight=1)
        self.ventana()
        self.construir_widget()

    def ventana(self):
        self.title("Calculadora_Algebraica")
        self.configure(bg="#1E1E1E")
        self.attributes("-alpha", 0.96)
        w, h = 700, 500
        utils.centrar_ventana(self, h, w)

    def construir_widget(self):
        self.pantalla_operacion = tk.Entry(self, width=25, font=(
            "Fira Code", 32, "bold"), bd=0, fg="#FFFFFF", bg="#2e2e3e", justify='right')
        self.pantalla_operacion.grid(row=1, column=0, columnspan=14, sticky="nsew")


        tk.Button(self, text="Resolver", width=11, height=2,
                  bg="#27AE60",activebackground="#2ECC71", fg="#FFFFFF", relief=tk.FLAT,command= self.resolver,  font=("Fira Code", 20, "bold"), padx=5, pady=5, bd=0,
                  borderwidth=0, highlightthickness=0,
                  overrelief='flat').grid(row=3, column=0, sticky="ew", columnspan=2, pady=5)

        self.resultado = tk.Label(self, text="", font=("Consolas", 14), fg="#B2FF59", bg="#1E1E1E")
        self.resultado.grid(row=4, column=0, sticky="ew", columnspan=8, pady=10 )

        ayuda_frame = tk.Frame(self, bg="#121212", padx=10, pady=10)
        ayuda_frame.place(relx=1.0, rely=1.0, anchor="se")

        ayuda_text = """\
        Expresiones válidas:
        • Suma/resta: 2x + 3 - 4
        • Potencia: x**2
        • Fracción: 1/x
        • Raíz: x**(1/2)
        • Log: log(numero, base)
        • Solo se puede utilizar: x,y,z
        """
        ayuda_label = tk.Label(ayuda_frame, text=ayuda_text, font=("Consolas", 10), fg="white", bg="#121212",
                               justify="left")
        ayuda_label.grid()

        botones = [
            "log(n, b)", "/","^","+", "-","√(1/)"
        ]

    def resolver(self):
        expresion = self.pantalla_operacion.get()
        resultado = logic.procesar_expresion(expresion)
        self.resultado.config(text=resultado)



