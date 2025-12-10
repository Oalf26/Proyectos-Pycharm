import app as game
from GoodApp import Game, GameAgain

app = game.app()
#app.empezar_juego()
#app.reinicio_juego()
#salir = input("\n🔚 Presiona Enter para salir... ")
juego = Game()
reiniciar = GameAgain
juego.empezar_juego()
reiniciar.volver_jugar()

