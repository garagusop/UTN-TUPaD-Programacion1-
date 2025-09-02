#EJERCICIO 1 
#Uso el bucle for para imprimir los numeros de 0 a 100 de 1 en 1
for num in range (0 , 101 , 1):
    print( num )

######################################################################################################

#EJERCICIO 2
#Pedimos un número entero
n = int(input ("Ingrese un numero entero"))
#inicializo el contador en 0
x = 0
#Mientras el número sea mayor que 0
while n > 0:
    #elimino el ultimo digito
    n=n // 10
    #sumo al contador
    x = x + 1
#muestro el resultado
print(f"El numero tiene {x} digitos")

######################################################################################################

#EJERCICIO 3
#Pido al usuario que ingrese los dos valores 
a = int(input("Ingrese el primer valor entero: "))
b = int(input("Ingrese el segundo valor entero: "))

#inicializo el contador en 0
total = 0

# uso for para imprimir los numeros comprendidos entre los datos ingresados
for numero in range(a + 1, b - 1):
    total = total + numero  #sumo al contador

#muestro el resultado
print(f"La suma de los enteros entre {a} y {b} es: {total}")

######################################################################################################

#EJERCICIO 4
#Inicializamos el total
total = 0

#Inicializamos la variable para el bucle
numero = int(input("Ingrese un entero : "))

while numero != 0:
    total = total + numero
    numero = int(input("Ingrese un entero : "))

# Mostramos el total acumulado
print(f"Total acumulado: {total}")


######################################################################################################

# EJERCICIO 5
#importo de la libreria
import random

#Genero el número a adivinar entre 0 y 9
adivina = random.randint(0, 9)

#Inicializamos el contador de intentos
intentos = 0

print("¡Adivina el número que tengo en mente! (del 0 al 9)")

#Inicializamos el intento con un valor que no este entre los que hay que adivinar
intento = 12  

# Repetimos mientras el usuario no adivine
while intento != adivina:
    intento = int(input("Tu intento: "))
    intentos = intentos + 1

    if intento == adivina:
        print(f"¡Adivinaste! El número era {adivina}")

# Mostramos la cantidad de intentos
print(f"Acertaste el numero en : {intentos} intentos")

######################################################################################################

#EJERCICIO 6
#Uso el bucle for para imprimir los numeros pares comprendidos entre 100 a 0 
for num in range (98 , 0 , -2):
    print( num )

######################################################################################################

#EJERCICIO 7 
#Pedimos al usuario un número entero positivo
num = int(input("Ingrese un número entero positivo: "))

#Inicializamos la suma
suma = 0

#Uso el bucle for para imprimir los numeros desde 0 hasta el numero ingresado y acumulamos
for x in range(0, num + 1):
    suma = suma + x

#Mostramos el total acumulado
print(f"La suma de los números entre 0 y {num} es: {suma}")

######################################################################################################

#EJERCICIO 8
#ingreso la cantidad de numeros a pedir al usuario
NUM = 100

#Inicializamos contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

#Usamos for in range para imprimir los numeros 
for x in range(1, NUM + 1):
    numero = int(input(f"Ingrese el entero {x}: "))

    #definimos numeros pares si el resto al dividir por 2 es 0
    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    #Contamos positivos y negativos
    if numero >= 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1

#Mostramos los resultados
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

######################################################################################################

#EJERCICIO 9
#ingreso la cantidad de numeros a pedir al usuario
NUM = 100

#Inicializamos acumulador
sumatotal = 0

#Leemos NUM valores y acumulamos
for x in range(1, NUM + 1):
    numero = int(input(f"Ingrese el entero {x}: "))
    sumatotal = sumatotal + numero

#Calculamos el promedio
promedio = sumatotal / NUM

#Mostramos el resultado
print(f"La media de los valores ingresados es: {promedio}")

######################################################################################################

#EJERCICIO 10
#Pedimos el número al usuario
numero = input("Ingrese un número: ")

# Invertimos el número usando slicing 
invertido = numero [::-1]

# Mostramos el resultado
print(f"El número invertido es: {invertido}")