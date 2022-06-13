
def calcular_iva():
    precio_producto = int(input("Ingrese el precio del producto: "))
    return precio_producto * 0.19
print("El iva del producto es:",calcular_iva())

def calcular_descuento():
    precio_producto = int(input("Ingrese el precio del producto: "))
    return precio_producto - precio_producto * 0.50
print("El producto tenía 50% de descuento, precio final:", calcular_descuento())

def calcular_imc():