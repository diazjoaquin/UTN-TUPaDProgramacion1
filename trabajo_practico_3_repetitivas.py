import random

def imprimir_numeros():
  for i in range(101):
    print(i)

def conta_digitos():
  numero = input("Ingrese un número: ")
  contador = 0
  for i in numero:
    contador = contador + 1
  print("El número tiene", contador, "dígitos")

def suma_intervalo():
  numero1 = int(input("Ingrese el primer número: "))
  numero2 = int(input("Ingrese el segundo número: "))
  resultado = 0
  for i in range(numero1 + 1, numero2, 1):
    resultado = resultado + i
  print("La suma del intervalo es:", resultado)

def suma_numeros():
  numero = int(input("Ingrese un número: "))
  resultado = 0 + numero

  while numero != 0:
    numero = int(input("Ingrese otro número (0 para terminar): "))
    resultado = resultado + numero
    print("La suma de los números ingresados es:", resultado)
  print("Fin del programa")

def adivinar_num():
  numero = int(input("Ingrese un número entre 0 y 9: "))
  randomNum = random.randint(0, 9)
  contador = 1
  if numero < 0 or numero > 9:
    numero = int(input("Número inválido. Ingrese un número entre 0 y 9: "))
  while (numero >= 0 and numero <= 9):
    if numero == randomNum:
      print("Adivinaste el numero!")
      print ("Intentos: ", contador)
      break
    else:
      numero = int(input("Vuelve a intentarlo: "))
      contador = contador + 1

def cien_a_cero():
  for i in range(100, -1, -1):
    print(i)

def suma_cero_a_num():
  numero = int(input("Ingrese un numero entero: "))
  acc = 0

  for i in range (1, numero + 1, 1):
    acc = acc + i
  print("La suma de los números desde 1 hasta", numero, "es:", acc)

def cien_nums():
  numero = int(input("Ingrese un número: "))
  contador = 1
  positivos = 0
  negativos = 0
  pares = 0
  impares = 0

  while contador < 100:
    if numero > 0:
      positivos = positivos + 1
    elif numero < 0:
      negativos = negativos + 1
    if numero % 2 == 0:
      pares = pares + 1
    else:
      impares = impares + 1
    contador = contador + 1
    numero = int(input("Ingrese otro número: "))
  print("Cantidad de números positivos:", positivos)
  print("Cantidad de números negativos:", negativos)
  print("Cantidad de números pares:", pares)
  print("Cantidad de números impares:", impares)
  
def promedio_nums():
  numero = int(input("Ingrese un número entero: "))
  contador = 1
  promedio = 0 + numero

  if (numero < 0):
    print("El número no es válido")
  else:
    while contador < 100:
      contador = contador + 1
      numero = int(input("Ingrese otro número: ")) 
      promedio = promedio + numero
    print("El promedio de los números ingresados es:", promedio / 100)

def invertir():
  numero = input("Ingrese un número: ")
  invertido = ""
  for i in range(len(numero) - 1, -1, -1):
    invertido = invertido + numero[i]
  print("El número invertido es:", invertido)


