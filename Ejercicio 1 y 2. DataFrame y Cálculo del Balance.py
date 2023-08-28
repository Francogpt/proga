"""
Nombre: Francisco Javier Lagunes Lopez 
Grupo: 651
Fecha: 08-27-2023
"""

# Ejercicio 1

"""
Descripción del problema: En este ejercicio lo que hice fue crear una 
función llamada generar_dataframe que, al ser llamada, genera 
un DataFrame basado en el diccionario datos que contiene información
sobre los meses, las ventas y los gastos. Finalmente, la función retorna 
este DataFrame y lo mostramos en pantalla con un print.
"""

import pandas as pd

def generar_dataframe():
    datos = {
        'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril'],
        'Ventas': [30500, 35600, 28300, 33900],
        'Gastos': [22000, 23400, 18100, 20700]
    }
    df = pd.DataFrame(datos)
    return df

df_ventas = generar_dataframe()
print("VENTAS\n", df_ventas)

# Ejercicio 2

"""
Descripción del problema: En este definí una función calculo_balance 
que recibe un DataFrame y una lista de meses. Esta función filtra el 
DataFrame con los meses proporcionados y luego calcula el balance 
(ventas menos gastos) para esos meses específicos. Finalmente, se suman 
todos los balances de los meses seleccionados y se retorna ese valor. 
En el código principal, simplemente llamamos a esta función y mostramos 
el balance total para todos los meses presentes en el DataFrame.
"""

def calculo_balance(df, meses):
    df_seleccionado = df[df['Mes'].isin(meses)]
    return (df_seleccionado['Ventas'] - df_seleccionado['Gastos']).sum()

meses_a_considerar = df_ventas['Mes']
balance_total = calculo_balance(df_ventas, meses_a_considerar)
print("\nBalance total para todos los meses:", balance_total)
