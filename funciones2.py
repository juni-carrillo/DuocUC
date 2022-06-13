#Otras funciones

"""Función varios_valores()que recibe una lista dinámica
de argumentos y por ello, se debe incluir un *.
Esto se llama recibir parámetros indeterminados por posición
"""
def varios_valores(*args):
    for arg in args:
        print(arg)

varios_valores(4.5, "Buen día", [1,2,3,4,5])

"""
Función mostrar_valores() que no recibe parámetros, sin embargo
retorna valores múltiples, esto se llama "Retorno múltiple"
"""
def mostrar_valores():
    return("Buen día", 15, [15,20,30])

print(mostrar_valores())