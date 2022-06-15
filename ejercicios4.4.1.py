import random
import numpy as np

def ejercicio_uno():
    p = [random.randint(0,100) for i in range(10)]
    print(p)

    i = int(input("Ingrese un número de 1 a 100, para ver si está en la lista: "))
    if i in p:
        print("Si está!")
    else:
        print("No está!")
ejercicio_uno() 
def ejercicio_dos():
    
    
    print("Los valores deben ser entre 3 y 6!\n")
    a = int(input("Ingrese el tamaño del eje x del arreglo: "))
    b = int(input("Ingrese el tamaño del eje y del arreglo: "))
    flag = True
    while flag:
        if a >= 3 and a <=6 and b >=3 and b <=6:
            randnums= np.random.randint(1,100, (a,b))
            print("\nArreglo poblado:\n",randnums,"\n")
            suma_filas = randnums.sum(axis=1)
            promedio_columnas = randnums.mean(axis=0)
            print("La suma de las filas es:",suma_filas)
            print("El promedio de las columnas es:",promedio_columnas)
        
        else:
            print("Ingrese un valor entre 3 y 6")
            break
            
ejercicio_dos()