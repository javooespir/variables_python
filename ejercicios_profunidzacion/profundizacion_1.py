# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
print("Los valores ingreados por el operador seran utilizados para calcular las siguientes operaciones, segun el orden de ingreso:"
"\nSuma"
"\nResta"
"\nMultiplicación"
"\nDivision"
"\nPotencia")

print("Por favor, ingrese el primer valor entero que desea utilizar:")
numero_1 = int(input())
print("Ahora ingrese el segundo valor entero a utilizar:")
numero_2 = int (input())

print("A continuacion, el resultado de las operaciones son:",
"\nLa suma entre", numero_1,"y",numero_2, "es:",numero_1 + numero_2,
"\nLa resta entre", numero_1,"y",numero_2, "es:",numero_1 - numero_2,
"\nLa multiplicación entre", numero_1, "y", numero_2, "es:", numero_1 * numero_2,
"\nLa división entre", numero_1, "y", numero_2, "es:", numero_1 / numero_2,
"\nLa potencia de", numero_1, "elevado a la", numero_2, "es:", numero_1 ** numero_2)

