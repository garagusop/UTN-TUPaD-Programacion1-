#EJERCICIO 1
#Uso la funcion print para mostrar un mensaje por pantalla
print(" Hola Mundo!.")

#EJERCICIO 2
#Uso la funcion input para pedirle al usuario que ingrese su nombre
nombre = input ("Por favor, escribe tu nombre: ")
#Uso la funcion print(f) para mostrar el nombre por pantalla
print (f"Hola {nombre}! ")

#EJERCICIO 3
#Uso la funcion input para pedirle al usuario que ingrese su nombre,apellido,edad y lugar de residencia
nombre = input ("Por favor, escribe tu nombre: ")
apellido = input ("Por favor, escribe tu apellido: ")
edad = input ("Por favor, escribe tu edad: ")
pais = input ("Por favor, escribe tu lugar de residencia: ")
#Uso la funcion print(f) para mostrar los datos ingresados por pantalla
print (f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {pais} ! ")

#EJERCICIO 4
#Uso la funcion input para pedir al usuario el radio del círculo
radio = input("Por favor, ingresa el radio del circulo: ")
#Convierto el dato ingresado a un numero decimal con float() 
radio = float(radio)
#Calculo el área y el perímetro
area =  3.1416 * radio * radio
perimetro = 2 * 3.1416 * radio
#Uso la funcion print(f) para mostrar el resultado por pantalla
print(f"El area del circulo es: {area} y el perimetro es: {perimetro}")

#EJERCICIO 5
#Uso la funcion input para pedirle al usuario que ingrese cantidad de segundos
segundos = input ("Por favor escribi la cantidad de segundos a convertir: ")
#Convierto el dato ingresado a un numero entero con int() 
segundos = int(segundos)
#Calculo las horas
horas = segundos / 3600
#Uso la funcion print(f) para mostrar el resultado por pantalla
print(f"Equivale a: {horas} horas")

#EJERCICIO 6
#Uso la funcion input para pedirle al usuario que ingrese un numero
numero = input ("Por favor escribi un numero: ")
#Convierto el dato ingresado a un numero entero con int() 
numero = int(numero)
#Uso la funcion print para mostrar el resultado por pantalla
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#EJERCICIO 7
#Uso la funcion input para pedirle al usuario que ingrese dos numeros distintos a cero
num1 = input("Escribi el primer numero (distinto de 0): ")
num2 = input("Escribi el segundo numero (distinto de 0): ")
#Convierto los datos ingresados a un numero entero con int() 
num1 = int(num1)
num2 = int(num2)
#Realizo las operaciones
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
#Uso la funcion print para mostrar el resultado por pantalla
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

#EJERCICIO 8
#Uso la funcion input para pedirle al usuario que ingrese su peso y altura
peso = input("Escribi tu peso en kg: ")
altura = input("Escribi tu altura en metros: ")
#Convierto los datos ingresados a numeros decimales con float() 
peso = float(peso)
altura = float(altura)
#Realizo el calculo con la formula
imc = peso / (altura * altura)
#Uso la funcion print para mostrar el resultado por pantalla
print(f"Tu indice de masa corporal (IMC) es: {imc} ")

#EJERCICIO 9
#Uso la funcion input para pedirle al usuario que ingrese una temperatura en grados Celsius
celsius = input("Por favor escribi la temperatura en grados Celsius: ")
#Convierto los datos ingresados a numeros decimales con float() 
celsius = float(celsius)
#Realizo el calculo con la formula
fahrenheit = (9 / 5) * celsius + 32
#Uso la funcion print para mostrar el resultado por pantalla
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}")

#EJERCICIO 10
#Uso la funcion input para pedirle al usuario que ingrese 3 numeros
num1 = input("Escribi el primer número: ")
num2 = input("Escribi el segundo número: ")
num3 = input("Escribi el tercer número: ")
#Convierto los datos ingresados a numeros decimales con float() 
num1 = float(num1)
num2 = float(num2)
num3 = float(num3)
#Realizo el calculo del promedio
promedio = (num1 + num2 + num3) / 3
#Uso la funcion print para mostrar el resultado por pantalla
print(f"El promedio es {promedio}")
