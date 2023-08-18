"""
Nombre: Francisco Javier Lagunes Lopez 
Grupo: 651
Fecha: 08-16-2023
Descripción del problema: para este ejercicio, hice básicamente 
lo opuesto que en "Encriptar". 
Usé un diccionario pero esta vez relacionando las letras de la clave 
con las del alfabeto básico. Luego, leí el mensaje letra por letra: 
si era una letra de la clave, la cambié por la que corresponde en el 
alfabeto básico usando el diccionario, y si no, la dejé tal cual. 
Al final, uní todo para devolver el mensaje original. Así logré revertir 
el proceso de encriptación. 
"""

def desencripta(s, clave):
    # Se crea un mapeo de la clave al alfabeto básico.
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    mapeo_inverso = {clave[i]: alfabeto[i] for i in range(26)}
    
    # Se recorre el mensaje y se desencripta cada letra.
    mensaje_decodificado = []
    for char in s:
        if char in mapeo_inverso:
            mensaje_decodificado.append(mapeo_inverso[char])
        else:
            mensaje_decodificado.append(char)
    
    return ''.join(mensaje_decodificado)

# Se prueba la funcion
texto1 = 'milk'
clave1 = 'ixmrklstnuzbowfaqejdcpvhyg'
print(desencripta(texto1, clave1))  

texto2 = 'riok 1 mtfmfbidk'
clave2 = 'ixmrklstnuzbowfaqejdcpvhyg'
print(desencripta(texto2, clave2))  


