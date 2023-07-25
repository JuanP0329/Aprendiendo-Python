#En este ejercicio tendréis que crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.

#Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.

def Sumar(a, b):
    return a + b

def Restar(a, b):
    return a - b

def Multiplicar(a, b):
    return a * b

def Dividir(a, b):
    if b == 0:
        return "Division entre cero no Existe"
    else:
        return a / b