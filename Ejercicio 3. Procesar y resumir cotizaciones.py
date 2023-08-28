"""
Nombre: Francisco Javier Lagunes Lopez 
Grupo: 651
Fecha: 08-27-2023
"""

# Ejercicio 3

"""
Descripción del problema: En este ejercicio se me solicito procesar 
las cotizaciones de diferentes empresas desde un archivo CSV alojado 
en una URL. Lo primero que hice fue definir una función llamada 
procesar_cotizaciones, que se encarga de cargar este archivo en un 
DataFrame. Luego, para cada columna del DataFrame, calculé el valor 
mínimo, el máximo y el promedio utilizando los métodos min(), max() 
y mean(). Estos cálculos los almacené en un diccionario resumen. 
Finalmente, generé un nuevo DataFrame (df_resumen) con este resumen y 
lo retorné. En el cuerpo principal del programa, llamé a la función 
con la URL dada y mostré el DataFrame resultante en pantalla.
"""
import pandas as pd
def procesar_cotizaciones(df_cotizacion):
  
    df_cotizacion = pd.read_csv('https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv')

    resumen = {
        'Mínimo': df_cotizacion.min(),
        'Máximo': df_cotizacion.max(),
        'Promedio': df_cotizacion.mean()
    }

    
    df_resumen = pd.DataFrame(resumen)
    return df_resumen


df_resultado = procesar_cotizaciones('https://aprendeconalf.es/docencia/python/ejercicios/soluciones/pandas/cotizacion.csv')
print(df_resultado)


