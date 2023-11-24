import pandas as pd
datos = pd.read_csv("surveys.csv")
#print(datos.sample(10))
nulos = datos.isnull()
#print(nulos.any())
#print(nulos.sum())
#print(nulos.sum().sum())
#print(nulos.sum()/len(nulos))

# eliminar columnas

datos_eliminados = datos.drop(["day", "month"], axis="columns")
#print(datos.columns)
print(datos_eliminados.columns)

# Eliminar columna original
datos.drop(["day", "month"], axis= "columns", implace=True)
#print(datos.columns)

datos_row_elim = datos.drop([2,3,4], axis="index")
#print(datos_row_elim.head(10))