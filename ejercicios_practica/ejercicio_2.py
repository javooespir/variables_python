# Tipos de variables [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de práctica numérica y consola

# Ahora los valores a operar deben ser ingresados por
# consola con la función "input" como se ve a continuación
from tkinter import N


print('Ingrese por consola el primer número entero a operar:')
numero_1 = int(input())

print('Ingrese por consola el segundo número entero a operar:')
numero_2 = int(input())

# Alumno: Imprima en pantalla los dos números enteros solicitados
'''Inicio Parte A!'''

print("El primer numero ingresado es:", numero_1,", y el segundo numero ingresado es:", numero_2)

# Alumno: Calcule la suma, resta, división y multiplicación de los números ingresados
# numero_1, numero_2
# Imprima en pantalla todos los resultados con el siguiente formato de ejemplo:
# El resultado de sumar 4 y 2 es 6
# NOTA: No coloque usted los nùmeros y resultados, use las variables

# Suma

# Resta

# División

# Multiplicación
'''Inicio Parte B!'''

suma = numero_1 + numero_2
resta = numero_1 - numero_2
division_int = numero_1 // numero_2
division_float = numero_1 / numero_2
multiplicacion = numero_1 * numero_2

print("El resultado de la suma es:", suma,
      "\nEl resultado de la resta es:", resta, 
      "\nEl resultado de la division con Nº enteros es:", division_int, 
      "\nEl resultado de la division exacta es:", division_float, 
      "\nEl resultado de la multiplicacion es:", multiplicacion) #\n lo utilizo para solo poner 1 funcion de print, y marcar el salto de linea en la consola
