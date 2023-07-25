#Ejercicio 1 Bibliotecas y funciones Built-in

#Crea un script que le pida al usuario una lista de países (separados por comas). 
#Éstos se deben almacenar en una lista. No debería haber países repetidos (haz uso de set). 
#Finalmente, muestra por consola la lista de países ordenados alfabéticamente y separados por comas.
paises = input("Ingrese una lista de países separados por comas: ")

lista_paises = paises.split(",")

conjunto_paises = set(lista_paises)

lista_paises_ordenada = sorted(list(conjunto_paises))

print("Lista de países ordenados alfabéticamente: ", end="")
print(*lista_paises_ordenada, sep=", ")

#Ejercicio 2 Bibliotecas y funciones Built-in

#En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por
#parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.
from functools import reduce

def suma_impares(lista):
    impares = filter(lambda x: x % 2 != 0, lista)
    suma = reduce(lambda a, b: a + b, impares)
    return suma

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = suma_impares(lista)
print(resultado) 
