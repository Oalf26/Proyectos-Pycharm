import app

app = app.app()
app.empezar_juego()
volver_jugar = input("¿Quieres volver a jugar? (s/n)")
if volver_jugar == "s":
    app.empezar_juego()
else:
    print("Gracias por juga!")
    salir = input("presione entrer para salir")