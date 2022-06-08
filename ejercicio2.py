import numpy as np

lista = np.random.randint(0,100, size=(3,3))
print(lista)
print(lista.mean())
print(lista.sum())
print(lista.max())
print(lista.min())
lista_diag = np.diag(lista)
print(lista_diag)

