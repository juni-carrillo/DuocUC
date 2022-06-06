opcion = int(input("Presione '1' para comenzar a ingresar nombres, presione '2' para salir.\n"))
nombres = []
i = 0
def continuar():
    continu = int(input("Desea continuar\n1. Si\n2. No\n"))
    if continu ==2:
        nombres_ordenado = sorted(nombres, key=lambda el: len(el))
        print(nombres_ordenado)
        print("¡ELIMINAREMOS EL NOMBRE CON MENOS CARACTERES!")
        print("El nombre eliminado fue:",nombres_ordenado.pop(0))
        print("Lista actual:",nombres_ordenado)
        exit()
        
    elif continu !=1 and continu !=2:
        print("Valor incorrecto.")
        return continuar()
while opcion == 1:
    i+=1
    item =input("Ingrese un nombre %d: "%i)
    if item=='':
        break
    nombres.append(item)
    print(nombres)
    continuar()
