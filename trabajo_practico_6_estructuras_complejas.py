# Práctica 6: Estructuras complejas
#1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print('Ejercicio 1: ')
print(precios_frutas)

#2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Pera'] = 2800

print('Ejercicio 2: ')
print(precios_frutas)

#3
new_list = precios_frutas.keys()
print('Ejercicio 3: ')
print(new_list)

#4
def agendar_contactos():
  contactos = {}
  for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el telefono del contacto: ")
    if nombre in contactos:
      print("El contacto ya existe")
    else:
      if telefono.isdigit():
        contactos[nombre] = telefono
        print(f"Contacto {nombre} con telefono {telefono} agregado")
      else:
        print("Ingrese un valor valido")
  
  consulta = input("Ingrese un nombre para consultar su telefono: ")
  if consulta in contactos:
    print(f"El telefono de {consulta} es {contactos[consulta]}")
  else:
    print("El contacto no existe")

#5
def palabras_unicas_y_contador_de_palabras(frase):
  if not frase:
    print("Ingrese una frase valida")
    return

  palabras = frase.replace(",", " ").replace(".", " ").split()
  palabras_unicas = set(palabras)
  print(f"Palabras unicas: {palabras_unicas}")

  palabras_contador = {}
  for i in palabras:
    if i in palabras_contador:
      palabras_contador[i] += 1
    else:
      palabras_contador[i] = 1
  print(f"Contador de palabras: {palabras_contador}")

input_frase = input("Ingrese una frase: ")
palabras_unicas_y_contador_de_palabras(input_frase)

#6
def alumnos_notas_y_promedio():
  alumnos = {}
  for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    notas = ()
    for j in range(3):
      nota = float(input(f"Ingrese la nota {j+1} del alumno {nombre}: "))
      notas += (nota,)
    alumnos[nombre] = notas
    
  print(alumnos)
  for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"El promedio de {nombre} es {promedio}")

# alumnos_notas_y_promedio()

#7 
def aprobacion_parciales():
  parcial_1 = {1, 2, 4, 6, 7, 10}
  parcial_2 = {2, 3, 6, 9, 5, 7}

  ambos_parciales = parcial_1.intersection(parcial_2)
  solo_uno = parcial_1.symmetric_difference(parcial_2)
  print(f"Estudiantes que aprobaron ambos parciales: {ambos_parciales}")
  print(f"Estudiantes que aprobaron solo uno de los parciales: {solo_uno}")
  print(f"Estudiantes que aprobaron al menos un parcial: {parcial_1.union(parcial_2)}")

# aprobacion_parciales()

#8
def mi_tienda():
  stock = {
    'Café': 5,
    'Té': 10,
    'Chocolate': 8,
    'Leche': 12,
    'Arroz': 6
  }

  print("Bienvenido a mi tienda: ingrese una opcion: ")
  print("1. Consultar stock")
  print("2. Agregar stock")
  print("3. Agregar nuevo producto")
  opcion = input("Ingrese una opcion: ")

  if opcion == '1':
    consultar_stock = input("Ingrese el nombre del prodcuto del cual desea consultar el stock: ")
    if consultar_stock in stock:
      print(f"El stock de {consultar_stock} es de {stock[consultar_stock]}")
    else:
      print("El producto no existe")
  elif opcion == '2':
    agregar_stock = input("Ingrese el nombre del producto el cual desea agregar al stock: ")
    if agregar_stock in stock:
      cantidad = int(input("Ingrese la cantidad de unidades a agregar: "))
      stock[agregar_stock] += cantidad
      print(f"Se ha agregado {cantidad} unidades de {agregar_stock} al stock")
      print(stock)
    else:
      print("El producto no existe")
  elif opcion == '3':
    nuevo_producto = input("Ingrese el nombre del nuevo producto a agregar: ")
    if nuevo_producto in stock:
      print("El producto ya existe")
    else:
      cantidad = int(input("Ingrese la cantidad de unidades del nuevo producto: "))
      stock[nuevo_producto] = cantidad
      print(f"Se ha agregado {nuevo_producto} con {cantidad} unidades al stock")
      print(stock)
  else:
    print("Opcion no valida")

# mi_tienda()

def crear_agenda():
  agenda = {}
  for i in range(3):
    dia = input("Ingrese el dia de la agenda: ")
    hora = input("Ingrese la hora de la agenda: ")
    evento = input("Ingrese el evento de la agenda: ")
    agenda[dia, hora] = evento

  # consultar la agenda
  dia_consulta = input("Ingrese el dia para consultar la agenda: ")
  actividades = [(hora, evento) for (dia, hora), evento in agenda.items() if dia == dia_consulta]
  if actividades:
    print(f"En {dia_consulta} tienes los siguientes eventos:")
    for hora, evento in actividades:
      print(f"{hora}: {evento}")
  else:
    print("No tienes eventos programados para ese dia")

# crear_agenda()

def invertir_diccionario():
  original = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Peru": "Lima",
    "Uruguay": "Montevideo",
    "Brasil": "Brasilia",
    "Paraguay": "Asunción",
    "Ecuador": "Quito",
    "Venezuela": "Caracas",
  }

  invertido = {}

  for pais, capital in original.items():
    invertido[capital] = pais

  print("Diccionario original: ")
  print(original)
  print("Diccionario invertido: ")
  print(invertido)

# invertir_diccionario()
