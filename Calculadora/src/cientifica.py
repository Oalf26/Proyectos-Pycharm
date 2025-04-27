import math
import re

def procesar_expresion(expresion):
    funciones_trigo = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan']
    otras_funciones = [
        'log', 'ln', 'abs', 'round', 'floor', 'ceil', 'factorial', 'sqrt', 'exp'
    ]

    for func in funciones_trigo:
        expresion = re.sub(
            rf'{func}\(([^()]+)\)',
            rf'math.{func}(math.radians(\1))',
            expresion
        )

    # Otras funciones normales
    for func in otras_funciones:
        expresion = re.sub(
            rf'{func}\(([^()]+)\)',
            rf'math.{func}(\1)',
            expresion
        )

    # Constantes
    expresion = re.sub(r'\bpi\b', 'math.pi', expresion)
    expresion = re.sub(r'\be\b', 'math.e', expresion)

    # Potencias
    expresion = expresion.replace('^', '**')

    return expresion


def evaluar_expresion(expresion):
    try:
        while expresion.count('(') > expresion.count(')'):
            expresion += ')'

        exp_procesada = procesar_expresion(expresion)
        resultado = eval(exp_procesada)
        return resultado
    except Exception as e:
        print("ERROR:", e)
        return "Error"
