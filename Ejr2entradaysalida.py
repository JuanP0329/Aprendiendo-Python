class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def get_info(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}"
    
mi_vehiculo = Vehiculo("Toyota", "Corolla", 2022)

import pickle

with open("vehiculo.pickle", "wb") as archivo:
    pickle.dump(mi_vehiculo, archivo)

with open("vehiculo.pickle", "rb") as archivo:
    vehiculo_cargado = pickle.load(archivo)

print(vehiculo_cargado.get_info())