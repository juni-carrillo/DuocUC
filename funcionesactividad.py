#1
def resta(a,b):
    return a - b

print(resta(30, 10))

#2
def resta (a, b):
    return a - b

print(resta(b=30, a=10))

#3
def funcion():
    return "Bienvenidos a Python"

frase = funcion()
print(frase)

#4
def resta(a=None, b=None):
    if a == None or b == None:
        print("Error, faltan parámetros a la función")
        return
    return a - b
resta()

#5
def calculo(precio, descuento):
    return precio - (precio * descuento / 100)

datos = [10000, 10]
print("El monto final a pagar es:", calculo(*datos))

#6
def saludo(nombre, mensaje="Python"):
    print(mensaje, nombre)

saludo(mensaje = "Buen día", nombre = "Pedro")

