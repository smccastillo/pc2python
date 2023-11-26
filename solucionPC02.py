#ESTRUCTURAS ITERATIVAS
#Problema 01
resultado=[]
for num in range(1500, 2701):
    if num % 7 == 0 and num % 5 == 0:
        resultado.append(num)

print("Números divisibles por 7 y múltiplos de 5:")
print(resultado)

#Problema 02
altura = 5

for i in range(altura):
    for j in range(i + 1):
        print("*",end="")
    print()

for i in range(altura - 1, 0, -1):
    for j in range(i):
        print("*",end="")
    print()

#Problema 03
list_num = []

while True:
    rpta = input("¿Desea ingresar un número?: ").upper()

    if rpta == "SI":
        num = int(input("Ingrese el número: "))
        list_num.append(num)
    elif rpta == "NO":
        break
    else:
        print("Ingrese una respuesta válida: SI o NO")

num_pares = 0
num_impares = 0

for a in list_num:
    if a % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1

print(f"Números ingresados: {list_num}")
print(f"Cantidad de números pares: {num_pares}")
print(f"Cantidad de números impares: {num_impares}")

#Problema 04
def alumnos_notas(n):
    lista_alumnos = []

    for i in range(n):
        nomb_alum = input(f"Ingrese el nombre del alumno {i+1}: ")

        notas = []
        for j in range(3):
            nota = float(input(f"Ingrese la calificación {j+1} para {nomb_alum}: "))
            notas.append(nota)

        alumno = {"Alumno": nomb_alum, "Notas": notas}

        lista_alumnos.append(alumno)

    return lista_alumnos

def listado_alumnos(lista_alumnos):
    print("\nLista de alumnos y sus notas:")
    for alumno in lista_alumnos:
        print(alumno)

cant = int(input("Ingrese la cantidad de alumnos: "))
alumnos = alumnos_notas(cant)
listado_alumnos(alumnos)

#FUNCIONES
#Problema 05
def contador_digitos(num, digito):
    numero = str(num)
    cantidad = numero.count(str(digito))

    # Imprime el resultado
    print(f"Número ingresado: {num} y Dígito: {digito}")
    print(f"Cantidad de veces {digito} en el número: {cantidad}")

num1 = input("Ingrese un número: ")
dig = input("Ingrese dígito a contar: ")

contador_digitos(num1, dig)

#Problema 06
def fibonacci(limite):
    a, b = 0, 1

    serie = [a]
    while b <= limite:
        serie.append(b)
        a, b = b, a + b

    return serie

num = int(input("Ingrese un número para mostrar la serie de Fibonacci: "))

resultado = fibonacci(num)
print(f"Serie de Fibonacci hasta {num}: {resultado}")

#Problema 07
def es_primo(num):
    if num <= 1:
        return False
    
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

a = int(input("Ingrese un número: "))
if es_primo(a):
    print(f"{a} es un número primo.")
else:
    print(f"{a} no es un número primo.")

#Problema 08
def factorial(numero):
    if numero < 0:
        return "Error: Ingrese un número válido mayor a 0"
    
    resultado = 1
    # Calcular el factorial del número
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

a = int(input("Ingrese un número para calcular su factorial: "))
resultado = factorial(a)
print(f"El factorial de {a} es: {resultado}")

#CADENAS
#Problema 09
def quitarvocales(cadena):
    cad = ""
    for caracter in cadena:
        if caracter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            cad += caracter
    return cad

frase = input("Ingrese una frase: ")

print("Frase sin las vocales:", quitarvocales(frase))