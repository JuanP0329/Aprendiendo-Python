# EJERCICIO #1 CLASES Y OBJETOS

#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
# -Color
# -Ruedas
# -Puertas

#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
# -Velocidad
# -Cilindrada

#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

class Vehiculo:
    def __init__(self, color, ruedas, puertas):
    
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

Mi_Coche = Coche("Blanco", 4, 5, "160Km/H", "CC 1000")

print("MI COCHE:")
print("Color:", Mi_Coche.color)
print("Ruedas::", Mi_Coche.ruedas)
print("Puertas", Mi_Coche.puertas)
print("Velocidad:", Mi_Coche.velocidad)
print("Cilindrada:", Mi_Coche.cilindrada)

# EJERCICIO #2 CLASES Y OBJETOS

#En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
#calificacion de 0-5
        if nota >= 3:
            print(nombre, "Felicidades!, APROBASTE con nota:", nota)

        elif nota > 5 or nota < 0:
            print("Digitaste una NOTA ERRONEA")

        else:
            print(nombre, "Malas noticias, NO APROBASTE con nota:", nota)

Alumno("Juan Carabali,", 4)

Alumno("Pedro Figueroa", 4.7)

Alumno("Daniel Gonzalez", 2.5)

#Ejercicio #2 MODULOS
import time

hora_actual = time.localtime().tm_hour

hora_fin_trabajo = 19  # 7:00 PM

if hora_actual >= hora_fin_trabajo:
    print("¡Es hora de ir a casa!")
else:
    tiempo_restante = (hora_fin_trabajo - hora_actual) * 60 - time.localtime().tm_min

    print("Aún no es hora de ir a casa. Quedan {} minutos.".format(tiempo_restante))

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

#Ejercicio #1 Interfaz de Usuarios
#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado y que contenga un botón de reinicio para que deje todo como al principio.

#Al principio no tiene que haber una opción seleccionada.

import tkinter

window = tkinter.Tk()

selected_option = tkinter.StringVar(value="")

def reset():
    selected_option.set("")

option1 = tkinter.Radiobutton(window, text="Opcion 1", variable=selected_option, value="Opcion 1")
option1.pack(ipadx=10, ipady=10, side="left")

option2 = tkinter.Radiobutton(window, text="Opcion 2", variable=selected_option, value="Opcion 2")
option2.pack(ipadx=10, ipady=10, side="left")

option3 = tkinter.Radiobutton(window, text="Opcion 3", variable=selected_option, value="Opcion 3")
option3.pack(ipadx=10, ipady=10, side="left")

reset_button = tkinter.Button(window, text="Reiniciar", command=reset)
reset_button.pack(ipadx=10, ipady=10, side="left")


window.mainloop()

#Ejercicio #2 Interfaz de Usuarios
#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.

import tkinter

window = tkinter.Tk()

label_texto = tkinter.Label(window, text="Selecciona un tema de tu preferencia:")
label_texto.pack()

lista = tkinter.Listbox(window)
lista.pack()

lista.insert(1, "Deportes")
lista.insert(2, "Gastronomia")
lista.insert(3, "Politica")
lista.insert(4, "Ciencia")

window.mainloop()