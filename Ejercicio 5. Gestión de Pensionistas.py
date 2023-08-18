"""
Nombre: Francisco Javier Lagunes Lopez 
Grupo: 651
Fecha: 08-16-2023
Descripción del problema: Para este ejercicio decidí hacer dos clases: 
una para el Pensionista y otra para el GrupoPensionistas. 
En la clase Pensionista, guardé los datos como identificador, 
nombre, edad y gastos. 
También añadí un método para calcular el promedio de gastos de un 
pensionista en particular. Luego, en la clase GrupoPensionistas, 
usé un diccionario para guardar a los pensionistas por su identificador, 
lo cual me permitió acceder rápidamente a cualquier pensionista por su 
identificador y hacer las operaciones necesarias. Los métodos que se
solicitaron los añadí en esta clase, y hice uso de funciones como 
sum(), min(), y max() para hacer los cálculos más fácilmente. 
"""

class Pensionista:
    def __init__(self, identificador, nombre, edad, gastos):
        self.identificador = identificador
        self.nombre = nombre
        self.edad = edad
        self.gastos = gastos

    def media_gastos(self):
        return sum(self.gastos) / len(self.gastos)


class GrupoPensionistas:
    def __init__(self):
        self.pensionistas = {}  # Diccionario para almacenar objetos Pensionista con clave identificador

    def agregar_pensionista(self, pensionista):
        self.pensionistas[pensionista.identificador] = pensionista

    def media_gastos(self, identificador):
        return self.pensionistas[identificador].media_gastos()

    def media_edad(self):
        total_edades = sum(p.edad for p in self.pensionistas.values())
        return total_edades / len(self.pensionistas)

    def edades_extremas(self):
        min_edad = min(self.pensionistas.values(), key=lambda p: p.edad)
        max_edad = max(self.pensionistas.values(), key=lambda p: p.edad)
        return min_edad, max_edad

    def suma_promedio(self):
        return sum(p.media_gastos() for p in self.pensionistas.values())

    def media_maxima(self):
        max_media = max(self.pensionistas.values(), key=lambda p: p.media_gastos())
        return max_media.media_gastos(), max_media.nombre, max_media.identificador

    def gasto_promedio(self):
        promedios = [p.media_gastos() for p in self.pensionistas.values()]
        return sorted(promedios)


# Creación de objetos y pruebas
carlos = Pensionista('1111A', 'Carlos', 68, [640, 589, 573])
grupo = GrupoPensionistas()
grupo.agregar_pensionista(carlos)
print(grupo.media_gastos('1111A'))  
