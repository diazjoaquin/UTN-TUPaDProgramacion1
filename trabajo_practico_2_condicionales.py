import random
from statistics import mode, median, mean

def edad():
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Es mayor de edad")

def nota():
    nota = int(input("Ingrese su nota: "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")

def numeroPar():
    numero = int(input("Ingrese un numero: "))
    if numero % 2 == 0:
        print("Ha ingresado un numero par")
    else:
        print("Por favor ingrese un numero par")

def categoriaPorEdad():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
      print("Niño/a")
    elif edad > 12 and edad < 18:
      print("Adolescente")
    elif edad >= 18 and edad < 30:
      print("Adulto joven")
    elif edad >= 30:
      print("Adulto")
    else:
      print("Edad no valida")

def contrasenia():
  contrasenia = input("Ingrese una contraseña de entre 8 a 14 caracteres: ")
  if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print("Contraseña correcta")
  else:
    print("Por favor ingrese una contraseña de entre 8 a 14 caracteres")


def statisctics():
  numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
  if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Sesgo positivo")
  elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Sesgo negativo")
  elif mean(numeros_aleatorios) == median(numeros_aleatorios) and median(numeros_aleatorios) == mode(numeros_aleatorios):
    print("Sin sesgo")

def palabra():
  palabra = input("Ingrese una palabra: ")
  vocales = ["a", "e", "i", "o", "u"]
  if palabra[len(palabra) - 1] in vocales:
    print(f"{palabra}!")
  else:
    print(f"{palabra}")

def nombreYOpcion():
  nombre = input("Ingrese su nombre: ")
  opcion = input("Ingrese una opcion: 1 para imprimir su nombre en mayuscula. 2 para imprimir su nombre en minuscula. 3 para imprimir su nombre con la primera letra en mayuscula.")

  if opcion == "1":
    print(nombre.upper())
  elif opcion == "2":
    print(nombre.lower())
  elif opcion == "3":
    print(nombre.capitalize())
  else:
    print("Opcion no valida")

def escalaTerremoto():
  magnitud = int(input("Ingrese la magnitud del terremoto: "))
  if magnitud >= 0 and magnitud < 3:
    print("Muy leve")
  elif magnitud >= 3 and magnitud < 4:
    print("Leve")
  elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
  elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
  elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
  elif magnitud >= 7:
    print("Extremo")
  else:
    print("Magnitud no valida")

def hemisferioYEpoca():
  hemisferio = input("Ingrese el hemisferio: Norte o Sur: ")
  mes = input("Ingrese el mes: Enero, Febrero, Marzo, Abril, Mayo, Junio, Julio, Agosto, Septiembre, Octubre, Noviembre, Diciembre: ")
  dia = int(input("Ingrese el dia: "))

  meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

  if dia < 1 or dia > 31:
    print("Dia no valido")
    pass

  if mes not in meses:
    print("Mes no valido")
    pass

  if hemisferio == "Norte":
    if mes == "Diciembre" and dia >= 21 or mes == "Enero" or mes == "Febrero" or mes == "Marzo " and dia <= 20:
      print("Invierno")
    elif mes == "Marzo" and dia >= 21 or mes == "Abril" or mes == "Mayo" or mes == "Junio" and dia <= 20:
      print("Primavera")
    elif mes == "Junio" and dia >= 21 or mes == "Julio" or mes == "Agosto" or mes == "Septiembre" and dia <= 20:
      print("Verano")
    elif mes == "Septiembre" and dia >= 21 or mes == "Octubre" or mes == "Noviembre" or mes == "Diciembre" and dia <= 20:
      print("Otoño")
  elif hemisferio == "Sur":
    if mes == "Diciembre" and dia >= 21 or mes == "Enero" or mes == "Febrero" or mes == "Marzo " and dia <= 20:
      print("Verano")
    elif mes == "Marzo" and dia >= 21 or mes == "Abril" or mes == "Mayo" or mes == "Junio" and dia <= 20:
      print("Otoño")
    elif mes == "Junio" and dia >= 21 or mes == "Julio" or mes == "Agosto" or mes == "Septiembre" and dia <= 20:
      print("Invierno")
    elif mes == "Septiembre" and dia >= 21 or mes == "Octubre" or mes == "Noviembre" or mes == "Diciembre" and dia <= 20:
      print("Primavera")
  else:
    print("Hemisferio no valido")

