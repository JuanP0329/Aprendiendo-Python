import tkinter


window = tkinter.Tk()

label1 = tkinter.Label(window, text="Posicionamiento absoluto", bg="blue", fg="white")
label1.place(x=10, y=50)

label1 = tkinter.Label(window, text="Posicionamiento absoluto", bg="red", fg="yellow")
label1.place(x=25, y=30)

window.mainloop()