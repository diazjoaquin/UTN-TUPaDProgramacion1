#1
# Creamos un archivo llamado "productos.txt" corriendo el script crear-archivo.sh

#2
print("2. Leyendo archivo y mostrando contenido")
file = open("Unidad 8 - Archivos/productos.txt", "r")
header = file.readline()
content = file.readlines()
for line in content:
    line = line.strip()
    if line:
        nombre, precio, cantidad = line.split(",")
        print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")

#3
print("3. Agregar un nuevo producto")
nombre = input("Ingrese el nombre del producto: ")
precio = input("Ingrese el precio del producto: ")
if precio.isdigit():
  precio = '$' + precio
  cantidad = input("Ingrese la canidad del producto: ")
  if cantidad.isdigit():
    with open("Unidad 8 - Archivos/productos.txt", "a") as file:
      file.write(f"\n{nombre},{precio},{cantidad}")
    print("Producto agregado")
  else:
    print("Ingrese un valor valido")
else:
  print("Ingrese un valor valido")

#4
print("4. Leer el archivo y crear una lista de diccionarios con los productos")
file = open("Unidad 8 - Archivos/productos.txt", "r")
header = file.readline()
content = file.readlines()
lista = []
for line in content:
  line = line.strip()
  if line:
    nombre, precio, cantidad = line.split(",")
    producto = {
      "Nombre": nombre,
      "Precio": precio,
      "Cantidad": cantidad
    }
    lista.append(producto)
print(lista)

#5
print("5. Buscamos un producto por nombre y lo mostramos")
busqueda = input("Ingrese el nombre del producto que quiere buscar: ")
file = open("Unidad 8 - Archivos/productos.txt", "r")
content = file.readlines()
exist = False
for line in content:
  line = line.strip()
  if line:
    nombre, precio, cantidad = line.split(",")
    if busqueda.lower() == nombre.lower():
      print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad}")
      exist = True
      break
if not exist:
  print("Producto no encontrado")


  

#6
print("6. Guardar los productos actualizados")
with open("Unidad 8 - Archivos/productos.txt", "w") as file:
  file.write(header)
  for producto in lista:
    file.write(f"{producto['Nombre']},{producto['Precio']},{producto['Cantidad']}\n")
  
file = open("Unidad 8 - Archivos/productos.txt", "r")
content = file.readlines()
print("Archivo actualizado: ", content)




