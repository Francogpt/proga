"""
Nombre: Francisco Javier Lagunes Lopez 
Grupo: 651
Fecha: 08-16-2023
Descripción del problema: Para este ejercicio he creado la clase 
Estadistica que tiene como atributo una lista de números. 
En el método frecuencia_numeros(), itero sobre la lista y cuento la 
frecuencia de cada número, guardando el resultado en un diccionario.
En el método moda(), reutilizo el método anterior para obtener el 
número que aparece más veces. 
Finalmente, en el método histograma(), itero sobre las frecuencias y 
uso asteriscos para representar cada aparición de un número. 
Ordeno el resultado para que los números aparezcan de menor a mayor 
en la salida. Con esto, puedo visualizar la distribución de números 
en la lista de manera gráfica. 
"""

class Estadistica:
    def __init__(self, numeros):
        self.numeros = numeros

    def frecuencia_numeros(self):
        frecuencia = {}
        for num in self.numeros:
            if num in frecuencia:
                frecuencia[num] += 1
            else:
                frecuencia[num] = 1
        return frecuencia

    def moda(self):
        frecuencia = self.frecuencia_numeros()
        return max(frecuencia, key=frecuencia.get)

    def histograma(self):
        frecuencia = self.frecuencia_numeros()
        for num, frec in sorted(frecuencia.items()):
            print(f"{num} {'*' * frec}")


# Ejemplo de uso
lista = Estadistica([1, 3, 2, 4, 2, 2, 3, 2, 4, 1, 2, 1, 2, 3, 1, 3, 1])
lista.histograma()
