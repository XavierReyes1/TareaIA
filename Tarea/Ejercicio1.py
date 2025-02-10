##1. Crea un programa que sume todos los números de una lista (sin usar el método nativo de Python “sum”).



def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

lista = [1, 2, 3, 4, 5]

print(suma_lista(lista))

