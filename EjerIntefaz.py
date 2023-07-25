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