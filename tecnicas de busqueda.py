import pandas as pd

Alumnos = {
    "nombre": ["Juan", "Maria", "Pedro", "Miguel"],
    "edad": [20, 19, 22, 18],
    "carrera": ["IN", "C", "NI", "IN",],
    "promedio": [90, 85, 70, 100]
}

df_alumnos = pd.DataFrame(Alumnos)

# Tecnica 1. filtrado de datos

c1 = df_alumnos.promedio > 80
data_c1 = df_alumnos[c1]
#print(data_c1)

c2 = (df_alumnos.promedio > 80) & ((df_alumnos.carrera == "IN") | (df_alumnos.carrera == "C"))
columnas = ["nombre", "carrera"]
data_c2 = df_alumnos[c2][columnas]
#print(data_c2)

# Tecnica 2. busqueda por query

query1_c1 = df_alumnos.query("promedio > 80")
#print(query1_c1)

condicion = "promedio > 80 and carrera.isin(['IN', 'C'])"
query2_c2 = df_alumnos.query(condicion)[columnas]
print(query2_c2)




