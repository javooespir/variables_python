# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejemplos variables de texto

# Ingrese dos palabras y arme combinaciones con ella
print('Ingrese palabra 1:')
palabra_1 = str(input())

print('Ingrese palabra 2:')
palabra_2 = str(input())

# De la primera palabra tome las primeras tres letras, utilice el operador :
# De la segunda palabra tome las primeras dos letras, utilice el operador :
# Formar una nueva palabra con los recortes solicitados
# Imprima en pantalla los resultados
'''Inicio del Ejercicio!'''
primeras_3_letras = palabra_1[:3]
primeras_2_letras = palabra_2[:2]

palabra_nueva = primeras_3_letras + primeras_2_letras

print("Las primeras 3 letras de la 1º palabra son:", primeras_3_letras)
print("Las primeras 2 letras de la 2º palabra son:", primeras_2_letras)
print("La nueva palabra sera:",palabra_nueva.upper())#.upper para que no importe si las palabras se escriben en minuscula o mayuscula