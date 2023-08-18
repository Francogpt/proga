"""
Nombre: Francisco Javier Lagunes Lopez 
Grupo: 651
Fecha: 08-16-2023
Descripción del problema: En este ejercicio de duplicado, creamos una función 
para averiguar si una lista tiene números repetidos.
Usé un set, que es como una bolsa donde solo puedes guardar cosas únicas. 
Mientras reviso cada número en la lista, miro si ya está en la bolsa. 
Si ya está, significa que es un duplicado y devuelvo True. Pero si no está, 
lo meto en la bolsa y sigo mirando el resto de los números. Si llego al
final de la lista y no he encontrado ningún número repetido, 
devuelvo False. Usar un set me ayudó porque buscar en él es súper rápido 
y así no tuve que comparar cada número con todos los demás en la lista. 
"""

def duplicados(nums):
    # Usamos un set para almacenar los números que ya hemos visto.
    visto = set()
    
    for num in nums:
        if num in visto:
            # Si el número ya está en el set, retornamos True
            return True
        visto.add(num)
    # Si no encontramos ningún duplicado, retornamos False
    return False

# Probamos la función
nums1 = [2, 2, 3, 1]
print(duplicados(nums1))  

nums2 = [1, 2, 6, 5]
print(duplicados(nums2))  
