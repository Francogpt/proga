"""
Nombre: Francisco Javier Lagunes Lopez 
Grupo: 651
Fecha: 08-27-2023
"""

# Ejercicio 4

"""
Descripción del problema: En este ejercicio analice un 
conjunto de datos sobre los pasajeros del Titanic. En el primer paso 
(A), simplemente cargué el conjunto de datos desde una URL en un DataFrame.
Después, en el paso (B), mostré las dimensiones del DataFrame. 
En el punto (C), presenté la cantidad total de datos y los nombres de sus 
columnas. Posteriormente, en el paso (D), visualicé las primeras y últimas 
10 filas del DataFrame para tener una idea general de los datos.
En el siguiente paso (E), calculé y mostré el porcentaje de sobrevivientes 
y fallecidos en el Titanic. Finalmente, en el paso (F), decidí analizar 
el porcentaje de sobrevivientes por clase del pasaje, para tener una idea 
de si la clase del pasaje influía en la posibilidad de supervivencia.
"""

import pandas as pd

# A) Generar un DataFrame con los datos del archivo
df_titanic = pd.read_csv('https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/titanic.csv')
print("A) Generar un DataFrame con los datos del archivo.\n")

# B) Mostrar las dimensiones del DataFrame
print("B) Dimensiones del DataFrame")
print(f" {df_titanic.shape[0]} filas y {df_titanic.shape[1]} columnas")

# C) Mostrar la cantidad total de datos y los nombres de las columnas
print("\nC) Mostrar el número de datos que contiene:", df_titanic.size, "\nNombres de sus columnas:", df_titanic.columns)

# D) Mostrar las 10 primeras y las 10 últimas filas
print("\nD) Mostrar las 10 primeras filas y las 10 últimas filas.")
print("Primeras 10 filas:\n", df_titanic.head(10))
print("\nÚltimas 10 filas:\n", df_titanic.tail(10))

# E) Mostrar el porcentaje de sobrevivientes y fallecidos
print("\nE) Mostrar porcentaje de sobrevivientes y fallecidos:")
survived_total = df_titanic['Survived'].sum()
total_pasajeros = df_titanic.shape[0]
sobrevivientes = (survived_total / total_pasajeros) * 100
fallecidos = 100 - sobrevivientes
print(f"Porcentaje de sobrevivientes: {sobrevivientes:.2f}%")
print(f"Porcentaje de fallecidos: {fallecidos:.2f}%")

# F) Mostrar el porcentaje de sobrevivientes por clase
print("\nF) Porcentaje de sobrevivientes en cada clase:")
survival_by_class = df_titanic.groupby('Pclass')['Survived'].mean() * 100
print(survival_by_class.round(0))
