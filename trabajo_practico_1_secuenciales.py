import math

# 1
def hello_world():
  print("Hola Mundo")

hello_world()

# 2
def saludar():
  nombre = input("Ingresa tu nombre: ")
  print(f"Hola {nombre}!")

saludar()

# 3
def presentar():
  nombre = input("Ingresa tu nombre: ")
  apellido = input("Ingresa tu apellido: ")
  edad = input("Ingresa tu edad: ")
  lugar_residencia = input("Ingresa tu lugar de residencia: ")

  print(f"Hola, soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

presentar()

# 4
def calcular_perimetro_circulo():
  radio = float(input("Ingresa el radio del circulo: "))
  pi = math.pi
  perimetro = 2 * pi * radio
  print(f"El perimetro del circulo es {perimetro}")

calcular_perimetro_circulo()

# 5
def segs_a_horas():
  segundos = int(input("Ingresa la cantidad de segundos: "))
  horas = segundos / 3600
  # podría ser // si quiero que sea un entero
  print(f"La cantidad de horas es {horas}")

segs_a_horas()

# 6
def tabla_multiplicar():
  numero = int(input("Ingrese un numero:"))
  for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar()

# 7
def operaciones_basicas():
  numero1 = int(input("Ingrese el primer numero: "))
  numero2 = int(input("Ingrese el segundo numero: "))

  if numero2 == 0 or numero1 == 0:
    print("Ingrese un numero valido")
    return
  
  suma = numero1 + numero2
  resta = numero1 - numero2
  multiplicacion = numero1 * numero2
  division = numero1 / numero2
  print(f"La suma de {numero1} y {numero2} es {suma}")
  print(f"La resta de {numero1} y {numero2} es {resta}")
  print(f"La multiplicacion de {numero1} y {numero2} es {multiplicacion}")
  print(f"La division de {numero1} y {numero2} es {division}")

operaciones_basicas()

# 8
def indice_masa_corporal():
  peso = float(input("ingresa tu peso en kg:"))
  altura = float(input("ingresa tu altura en metros:"))
  imc = peso / (altura ** 2)

  print(f"Tu indice de masa corporal es {imc}")

indice_masa_corporal()

# 9
def celcius_a_fahrenheit():
  celcius = float(input("ingresa la temperatura en grados celcius: "))
  fahrenheit = (celcius * 9/5) + 32

  print(f"La temperatura ingresada en grados fahrenheit es {fahrenheit}")

celcius_a_fahrenheit()

# 10
def calcular_promedio():
  numero1 = float(input("ingresa el primer numero: "))
  numero2 = float(input("ingresa el segundo numero: "))
  numero3 = float(input("Ingresa el tercer numero:"))

  promedio = (numero1 + numero2 + numero3) / 3
  print(f"El promedio de los numeros ingresados es {promedio}")

calcular_promedio()