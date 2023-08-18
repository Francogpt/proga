"""
Nombre: Francisco Javier Lagunes Lopez 
Grupo: 651
Fecha: 08-16-2023
Descripción del problema: Para resolver el ejercicio de suma de dos numeros, 
utilicé un diccionario. A medida que recorro la lista, voy pensando: 
"Si tengo este número, ¿cuánto me falta para llegar al target?".
Luego, veo si ese "número faltante" ya lo he visto antes en la lista.
Si ya lo vi, eso quiere decir que juntos suman al target y puedo dar 
la respuesta. Si no lo he visto, guardo el número que estoy revisando 
en el diccionario para considerarlo en el futuro. El diccionario me 
ayuda a encontrar los números rápidamente sin tener que revisar toda 
la lista de nuevo.
"""

def busquedaSuma(nums, target):
    # diccionario para mapear un número a su índice en la lista.
    indices = {}
    
    for i, num in enumerate(nums):
        # Se Calcula cuánto nos falta para llegar al target.
        complemento = target - num
        
        # Si el complemento ya está en el diccionario, Se a encontrado 
        #una solución.
        if complemento in indices:
            return (indices[complemento], i)
        
        # De lo contrario, se guarda el número y su índice en el diccionario.
        indices[num] = i

# Se prueba la función 
nums1 = [2, 7, 11, 15]
target1 = 9
print(busquedaSuma(nums1, target1))  

nums2 = [3, 2, 4]
target2 = 6
print(busquedaSuma(nums2, target2))  
