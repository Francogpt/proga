"""
Nombre: Francisco Javier Lagunes Lopez 
Grupo: 651
Fecha: 08-16-2023
Descripción del problema: para este ejercicio, hice un diccionario 
para relacionar cada letra del alfabeto básico con la 
letra correspondiente de la clave.
Después, fui letra por letra del mensaje: si era una letra del alfabeto, 
la cambiaba por la que decía el diccionario, y si no 
(como números o signos de puntuación), la dejaba igual. 
Al final, junté todas las letras y caracteres transformados para 
formar el mensaje codificado. Así conseguí que el mensaje se encriptara.
"""

def encripta(s, clave):
    # Se crea un mapeo del alfabeto básico a la clave.
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    mapeo = {alfabeto[i]: clave[i] for i in range(26)}
    
    # Se recorre el mensaje y se encripta cada letra.
    mensaje_codificado = []
    for char in s:
        if char in alfabeto:
            mensaje_codificado.append(mapeo[char])
        else:
            mensaje_codificado.append(char)
    
    return ''.join(mensaje_codificado)

# Se prueba la función 
texto1 = 'cafe'
clave1 = 'ixmrklstnuzbowfaqejdcpvhyg'
print(encripta(texto1, clave1))  

texto2 = 'dame 1 chocolate'
clave2 = 'ixmrklstnuzbowfaqejdcpvhyg'
print(encripta(texto2, clave2))  
