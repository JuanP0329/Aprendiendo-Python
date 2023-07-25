import tkinter

window = tkinter.Tk()

#meter mi geometria aca, antes de mi mainloop
#widge label
label_saludo = tkinter.Label(window, text="Hola!", bg="yellow", fg="blue")
#utilizamos la geometria pack
label_saludo.pack(ipadx=30, ipady=30, side="left")

label_adios = tkinter.Label(window, text="Adios", bg="red", fg="white")

label_adios.pack(ipadx=30, ipady=30, side="right")

window.mainloop()