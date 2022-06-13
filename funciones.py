
#Sin argumentos y sin retorno
def saludo():
    print("Saludando a mis estudiantes")

saludo()


#Sin argumentos y con retorno
def sumar():
    num1 = 3
    num2 = 5
    return(num1 + num2)

print("La suma es:",sumar())

#Con argumentos y sin retorno
def sumar(a, b):
    suma = a + b
    print(f'La suma de los argumentos es: {suma}')

num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))
sumar(num1, num2)

#Con argumentos y con retorno
def sumar(a, b):
    suma = a + b
    return(suma)

num1 = int(input("Ingrese primer número: "))
num2 = int(input("Ingrese segundo número: "))
print(f"El resultado de la suma es:", sumar(num1, num2))

