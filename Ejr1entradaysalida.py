with open("archivo.txt", "w") as f:
    f.write("Hola, este es un archivo de texto.\n")
    f.write("Aqui se puede escribir cualquier cosa.\n")

with open("archivo.txt", "r") as f:
    contenido = f.read()
    print(contenido)