import random

def notas():
  notas = [8.1, 7.5, 9.0, 6.8, 8.5, 7.2, 8.8, 9.3, 4.2, 4]
  print("Notas de los estudiantes:")
  print(notas)
  print("Promedio de las notas:", sum(notas) / len(notas))
  notas.sort()
  print("Nota mas alta: ", notas[-1])
  print("Nota mas baja: ", notas[0])

def productos():
  productos = []
  for i in range(5):
    producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)
  productos.sort()
  print("Productos ordenados:")
  print(productos)

  eliminar = input("Ingrese el nombre del producto a eliminar: ")
  if eliminar in productos:
    productos.remove(eliminar)
    print("Producto eliminado")
    print(productos)
  else:
    print("Producto no encontrado")

  modificar = input("Ingrese el nombre del producto a modificar: ")
  if modificar in productos:
    indice = productos.index(modificar)
    productos[indice] = input("Ingrese el nuevo nombre del producto: ")
    print("Producto modificado")
    print(productos.sort())
  else:
    print("Producto no encontrado")

def aleatorios():
  nums_aleatorios = []
  par = []
  impar = []
  for i in range(15):
    nums_aleatorios.append(random.randint(1, 100))
    if nums_aleatorios[i] % 2 == 0:
      par.append(nums_aleatorios[i])
    else:
      impar.append(nums_aleatorios[i]) 
  print(nums_aleatorios)
  print("Cantidad de numeros pares: ", len(par))
  print("Lista de numeros pares: ", par)
  print("Cantidad de numeros impares: ", len(impar))
  print("Lista de numeros impares: ", impar)

def remove_repetidos():
  datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
  set_datos = set(datos)
  list_datos = list(set_datos)
  print("Lista original: ", datos)
  print("Lista sin repetidos: ", list_datos)

def remove_estudiantes():
  estudiantes = ["Juan", "María", "Joaquín", "David", "Mónica", "Sol", "Gabriel", "Franco"]
  print("Lista de estuidantes: ", estudiantes)
  eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
  if eliminar in estudiantes:
    estudiantes.remove(eliminar)
    print("Estudiante eliminado")
    print(estudiantes)
  else:
    print("Estudiante no encontrado")
  
  modificar = input("Ingrese el nombre del estudiante a modificar: ")
  if modificar in estudiantes:
    indice = estudiantes.index(modificar)
    estudiantes[indice] = input("Ingrese el nuevo nombre del estudiante: ")
    print("Estudiante modificado")
    print(estudiantes)
  else:
    print("Estudiante no encontrado")

def rotar_derecha():
  lista = []
  for i in range(7):
    random_num = random.randint(1, 100)
    lista.append(random_num)
  print("Lista original: ", lista)
  lista.insert(0, lista[-1])
  lista.pop()
  print("Lista rotada: ", lista)

def matriz_temperaturas():
  matriz = []
  for i in range(7):
    fila = []
    for j in range(2):
      fila.append(random.randint(10, 25))
      fila.sort()
    matriz.append(fila)
  print(matriz)

  for k in range (7):
    minima = []
    minima.append(matriz[k][0])
    maxima = []
    maxima.append(matriz[k][1])
  print("Promedio de minimas temperaturas de la semana: ", sum(minima)/7)
  print("Promedio de maximas temperaturas de la semana: ", sum(maxima)/7)

  temp_maxima = 0
  for l in matriz:
    if l[1] > temp_maxima:
      temp_maxima = l[1]
  print("Temperatura maxima de la semana: ", temp_maxima)

def notas_estudiantes():
  notas = []
  for i in range(5):
    alumno = []
    for j in range(3):
      alumno.append(random.randint(1, 10))
    notas.append(alumno)

  print(notas)

  notas_alumno = 0
  promedio_materia = 0
  for i in range(5):
    notas_alumno = sum(notas[i])
    print("Promedio del alumno ",i+1, ": ",notas_alumno/3)

  for i in range(3):
    promedio_materia = 0
    for j in notas:
      promedio_materia += j[i]
    print("Promedio de la materia ", i+1, ": ",promedio_materia/5)

def ta_te_ti():
  tablero = []
  for i in range(3):
    fila = []
    for j in range(3):
      fila.append("-")
    tablero.append(fila)
  print(tablero)

  posx_jugador1 = int(input("Ingrese la posición horizontal en la que colocará X (1, 2 o 3): "))
  posy_jugador1 = int(input("Ingrese la posición vertical en la que colocará X (1, 2 o 3): "))
  if (posx_jugador1 > 3 or posy_jugador1 > 3 or posx_jugador1 <= 0 or posy_jugador1 <= 0):
    print("Posición inválida")
  else:
    if (tablero[posx_jugador1 - 1][posy_jugador1 - 1] == "-"):
      tablero[posx_jugador1 - 1][posy_jugador1 - 1] = "X"
    else:
      print("Posición ocupada")
      posx_jugador1 = int(input("Ingrese la posición horizontal en la que colocará X (1, 2 o 3): "))
      posy_jugador1 = int(input("Ingrese la posición vertical en la que colocará X (1, 2 o 3): "))
  print(tablero)

  posx_jugador2 = int(input("Ingrese la posición horizontal en la que colocará O (1, 2 o 3): "))
  posy_jugador2 = int(input("Ingrese la posición vertical en la que colocará O (1, 2 o 3): "))
  if (posx_jugador2 > 3 or posy_jugador2 > 3 or posx_jugador2 <= 0 or posy_jugador2 <= 0):
    print("Posición inválida")
  else:
    tablero[posx_jugador2 - 1][posy_jugador2 - 1] = "O"
  print(tablero)

def registro_ventas():
  dias = []
  for i in range(7):
    productos = []
    for j in range(4):
      productos.append(random.randint(1, 100))
    dias.append(productos)
  print(dias)


  producto_mayor_venta = 0
  venta_x_producto = []

  for i in range(4):
    total_vendido_producto = 0
    for j in dias:
      total_vendido_producto += j[i]
    print("Total vendido del producto ", i+1, ": ", total_vendido_producto)
    venta_x_producto.append(total_vendido_producto)
    if total_vendido_producto > producto_mayor_venta:
      producto_mayor_venta = total_vendido_producto
  print("Producto con mayor venta: (producto", venta_x_producto.index(producto_mayor_venta)+1, ") con un total de ", producto_mayor_venta, " unidades.")

  mayor_venta = 0
  dias_x_venta = []

  for i in dias:
    ventas_por_dia = 0
    for j in range(4):
      ventas_por_dia += i[j]
    print("Ventas por dia: ", ventas_por_dia)
    dias_x_venta.append(ventas_por_dia)
    if ventas_por_dia > mayor_venta:
      mayor_venta = ventas_por_dia
  print("Día con mayor venta: (día",dias_x_venta.index(mayor_venta)+1,") con un total de ", mayor_venta, " unidades.")