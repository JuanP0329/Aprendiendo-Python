class Dino:

    def __init__(self):
        print("Estoy en el constructor de Dino()")
        


#constructor

class Juguete(Dino):

    def __init__(self, nombre):
        super().__init__()
        print("Estoy en el constructor de Juguete", nombre)
        
        
Juguete("Juan")

#Clases Abstractas

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sonido(self):
        pass

    def diHola(self):
        print("Hola")

class Perro(Animal):
    def sonido(self):
        print("Guauuu")

class Gato(Animal):
    def sonido(self):
        print("Miauuu")

p = Perro()
p.sonido()
p.diHola()

g = Gato()
g.sonido()
g.diHola()