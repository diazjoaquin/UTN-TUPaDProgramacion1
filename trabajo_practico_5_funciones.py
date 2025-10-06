import math

#1
def imprimir_hola_mundo():
  print("Hola Mundo!")

imprimir_hola_mundo()

#2
def saludar_usuario(nombre):
  print(f"Hola, {nombre}!")

nombre = input("Ingrese su nombre: ")
saludar_usuario(nombre)

#3
def informacion_personal(nombre, apellido, edad, residecia):
  if edad.isdigit():
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residecia}")
  else:
    print("Ingrese valores validos")

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residecia = input("Ingrese su residecia: ")
informacion_personal(nombre, apellido, edad, residecia)

#4
def calcular_area_circulo(radio):
  if radio.isdigit():
    radio = int(radio)
    area = math.pi * radio**2
    print(f"El area del circulo es: {area}")
  else:
    print("Ingrese un radio valido")

def calcular_perimetro_circulo(radio):
  if radio.isdigit():
    radio = int(radio)
    perimetro = 2 * math.pi * radio
    print(f"El perimetro del circulo es: {perimetro}")
  else:
    print("Ingrese un radio valido")

radio = input("Ingrese el radio del circulo: ")
calcular_area_circulo(radio)
calcular_perimetro_circulo(radio)

#5
def segundos_a_horas(segundos):
  if segundos.isdigit():
    segundos = int(segundos)
    horas = segundos / 3600
    print(f"{segundos} segundos son {horas} horas")
  else:
    print("Ingrese un valor valido")

segundos = input("Ingrese la cantidad de segundos: ")
segundos_a_horas(segundos)

#6
def tabla_multiplicar(numero):
  if numero.isdigit():
    for i in range (1, 11):
      print(f"{numero} x {i} = {int(numero) * i}")
  else:
    print("Ingrese un valor valido")

numero = input("Ingrese un numero para ver su tabla de multiplicar: ")
tabla_multiplicar(numero)

#7
def operaciones_basicas(a,b):
  if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    if b != 0:
      print(f"{a} / {b} = {a / b}")
    else:
      print("No se puede dividir por cero")
  else:
    print("Ingrese valores validos")

a = input("Ingrese un numero: ")
b = input("Ingrese otro numero: ")
operaciones_basicas(a,b)

#8
def calcular_imc(peso, altura):
  if peso.isdigit() and (altura.isdigit() or altura.replace(".", "", 1).isdigit()):
    peso = int(peso)
    altura = float(altura)
    imc = peso / (altura**2)
    print(f"Su IMC es: {imc}")
  else:
    print("Ingrese valores validos")

peso = input("Ingrese su peso en kg: ")
altura = input("Ingrese su altura en metros: ")
calcular_imc(peso, altura)

#9
def celcius_a_fahrenheit(celcius):
  if celcius.isdigit():
    celcius = int(celcius)
    fahrenheit = (celcius * 9/5) + 32
    print(f"{celcius} grados Celsius son {fahrenheit} grados Fahrenheit")
  else:
    print("Ingrese un valor valido")

celcius = input("Ingrese una temperatura en grados Celsius: ")
celcius_a_fahrenheit(celcius)

#10
def calcular_promedio(a, b, c):
  if a.isdigit() and b.isdigit() and c.isdigit():
    a = int(a)
    b = int(b)
    c = int(c)
    promedio = (a + b + c) / 3
    print(f"El promedio de {a}, {b} y {c} es: {promedio}")
  else:
    print("Ingrese valores validos")

a = input("Ingrese un numero: ")
b = input("Ingrese otro numero: ")
c = input("Ingrese otro numero: ")
calcular_promedio(a, b, c)