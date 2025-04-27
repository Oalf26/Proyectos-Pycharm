from sympy import symbols, simplify, Eq, solve
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application

transformaciones = standard_transformations + (implicit_multiplication_application,)
x, y, z = symbols('x y z')
def procesar_expresion(expresion: str) -> str:
    try:
        if "=" in expresion:
            izquierda, derecha = expresion.split("=")
            izquierda = parse_expr(izquierda, transformations=transformaciones)
            derecha = parse_expr(derecha, transformations=transformaciones)
            ecuacion = Eq(izquierda, derecha)
            solucion = solve(ecuacion)
            return f"Solución: {solucion}"
        else:
            expre = parse_expr(expresion, transformations=transformaciones)
            resultado = simplify(expre)
            return f"Simplificado: {resultado}"
    except Exception as e:
        return f"Error: {str(e)}"