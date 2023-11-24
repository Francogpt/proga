import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

alumnos = {"nombre": [" Juan", " Maria ", "Josue  ", "Selene"],
           "genero": ["IN", "F", "N", "F"],
           "escolaridad": ["Universidad", "Universidad", "Prepa", "Secundaria"],
           }

data = pd.DataFrame(alumnos)
data["nombre"] = data.nombre.str.strip().str.upper()
data["nom_min"] = data.nombre.str.lower()
data["nom_may"] = data.nombre.str.upper()
data["X"] = data.nombre.str.lower().str.replace("A", "")

#metodos filtros
filtro_m = data.nombre.str.startswith("M")
#print(filtro_m)
#print(data[filtro_m])
end_e = data.nombre.str.endswith("E")
#print(end_e)
#print(data[end_e])
contiene_a = data.nombre.str.contains("A")
#print(data[contiene_a])

# Transformacion de metodos nominales
one_hot_enconder = pd.get_dummies(data.genero)
print(one_hot_enconder)

data = data.join(one_hot_enconder)


#trasformar datos ordinales
encoder = OrdinalEncoder(categories=[["Secundaria", "Prepa", "Universidad"]])
encoder.fit(data[["escolaridad"]])
data["educacion_encoder"] = encoder.transform(data[["escolaridad"]])
print(data)

