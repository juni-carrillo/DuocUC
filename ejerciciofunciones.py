
def calcular_iva():
    precio_producto = int(input("Ingrese el precio del producto: "))
    print("El iva del producto es:",(precio_producto * 0.19))

def calcular_descuento():
    precio_producto = int(input("Ingrese el precio del producto: "))
    print("El producto tenía 50% de descuento, precio final:",(precio_producto - precio_producto * 0.50))

def calcular_imc():
    peso = int(input("Ingrese su peso en kg: "))
    altura = float(input("Ingrese su altura en m: "))
    imc = peso/(altura*2)
    print("Su indice de masa corporal es:",imc)
    if imc < 18.5:
        print("Bajo peso.")
    elif imc >=18.5 and imc <=24.9:
        print("Peso adecuado.")
    elif imc >=25.0 and imc <=29.9:
        print("Obesidad grado 1.")
    elif imc >=30.0 and imc <=34.9:
        print("Obesidad grado 2.")
    elif imc >=40.0:
        print("Obesidad grado 3.")
    return imc



flag = True

while flag:
    menures = int(input("Eliga una opción:\n1. Calcular Iva.\n2. Calcular descuento.\n3. Calcular IMC.\n4. Salir\n"))
    
    
    if menures == 1:
        calcular_iva()
    
    elif menures == 2:
        calcular_descuento()
    
    elif menures == 3:
        calcular_imc()

    elif menures == 4:
        flag = False

    else:
        print("Ingrese una opción correcta.")



