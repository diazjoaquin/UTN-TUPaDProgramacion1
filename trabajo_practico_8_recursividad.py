# 1. Factorial
def factorial(n):
  return 1 if n == 0 else n * factorial(n - 1)

number = (input("Ingrese un número: "))
if number.isnumeric():
  number = int(number)
  for i in range(1, number + 1, +1):
    print(f"{i}! = {factorial(i)}")
else:
  print("Ingrese un número valido")

#2 Fibonacci
def fibonacci(n):
  return 0 if n == 0 else 1 if n == 1 else fibonacci(n - 1) + fibonacci(n - 2)

number = (input("Ingrese un número: "))
if number.isnumeric():
  number = int(number)
  for i in range(0, number + 1, +1):
    print(f"fibonacci({i}) = {fibonacci(i)}")
else:
  print("Ingrese un número valido")

#3
def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia_recursiva(base, exponente - 1)


base_input = input("Ingrese la base: ")
exponente_input = input("Ingrese el exponente: ")

if base_input.isnumeric() and exponente_input.isnumeric():
    base = int(base_input)
    exponente = int(exponente_input)
    if exponente >= 0:
        resultado = potencia_recursiva(base, exponente)
        print(f"{base}^{exponente} = {resultado}")
    else:
        print("El exponente debe ser un número entero positivo o cero")
else:
    print("Ingrese valores numéricos válidos")

# 4.
def binario_recursivo(decimal):
    if decimal == 0:
        return "0"
    elif decimal == 1:
        return "1"
    else:
        return binario_recursivo(decimal // 2) + str(decimal % 2)

decimal = input("Ingrese un número decimal: ")
if decimal.isnumeric():
  decimal = int(decimal)
  print(f"El número decimal {decimal} en binario es {binario_recursivo(decimal)}")
else:
  print("Ingrese un número decimal valido")

# 5.
def es_palindromo(palabra):
  if len(palabra) == 1:
    return True
  else:
    return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])

palabra = input("Ingrese una palabra: ")
if es_palindromo(palabra):
  print(f"{palabra} es un palíndromo")
else:
  print(f"{palabra} no es un palíndromo")

# 6.
def suma_digitos(n):
  return n if n < 10 else n % 10 + suma_digitos(n // 10)

n = input("Ingrese un número: ")
if n.isnumeric():
  n = int(n)
  print(f"La suma de los dígitos de {n} es {suma_digitos(n)}")
else:
  print("Ingrese un número valido")

# 7.
def contar_bloques(n):
  return 1 if n <= 1 else n + contar_bloques(n - 1)

n = input("Ingrese un número: ")
if n.isnumeric():
  n = int(n)
  print(f"La cantidad de bloques de {n} es {contar_bloques(n)}")
else:
  print("Ingrese un número valido")

# 8.
def contar_digito(numero_str, digito_str):
    if len(numero_str) == 0:
        return 0
    elif numero_str[0] == digito_str:
        return 1 + contar_digito(numero_str[1:], digito_str)
    else:
        return contar_digito(numero_str[1:], digito_str)


n = input("Ingrese un número: ")
if n.isnumeric():
    digito = input("Ingrese un dígito (0-9): ")
    if len(digito) == 1 and digito.isdigit():
        resultado = contar_digito(n, digito)
        print(f"La cantidad de veces que aparece el dígito {digito} en {n} es {resultado}")
    else:
        print("Ingrese un dígito válido (0-9)")
else:
    print("Ingrese un número válido")