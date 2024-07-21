""""
Generaremos un programa menu que realice las siguiente tareas.

1. Saludar
2. Calcular el factorial de un numero
3. Calcular el area de un circulo
4. Suma de divisores de un numero
5. Generar un triangulo rectangulo
6. Salir
"""
#1
import math
#2 constantes
# se puede poner de constante al menu

# 3. Definimos Funciones y/o clases

def saludar():
    print("¡Hola! Bienvenido al programa.")

def calcular_factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n - 1)

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def suma_divisores(n, i=1, suma=0):
    if i == n:
        return suma
    if n % i == 0:
        suma += i
    return suma_divisores(n, i + 1, suma)

def generar_triangulo_rectangulo(altura, nivel=1):
    if nivel > altura:
        return
    print('*' * nivel)
    generar_triangulo_rectangulo(altura, nivel + 1)

# 4. Definimos la función principal
def main():
    while True:
        print("\nMenú:")
        print("1. Saludar")
        print("2. Calcular el factorial de un número")
        print("3. Calcular el área de un círculo")
        print("4. Suma de divisores de un número")
        print("5. Generar un triángulo rectángulo")
        print("6. Salir")
        
        opcion = input("Selecciona una opción (1-6): ")
        
        if opcion == '1':
            saludar()
        
        elif opcion == '2':
            try:
                n = int(input("Introduce un número: "))
                print(f"El factorial de {n} es {calcular_factorial(n)}")
            except ValueError:
                print("Por favor, introduce un número entero válido.")
        elif opcion == '3':
            try:
                radio = float(input("Introduce el radio del círculo: "))
                print(f"El área del círculo con radio {radio} es {calcular_area_circulo(radio):.2f}")
            except ValueError:
                print("Por favor, introduce un número válido.")
        
        elif opcion == '4':
            try:
                n = int(input("Introduce un número: "))
                print(f"La suma de los divisores de {n} es {suma_divisores(n)}")
            except ValueError:
                print("Por favor, introduce un número entero válido.")
        
        elif opcion == '5':
            try:
                altura = int(input("Introduce la altura del triángulo: "))
                generar_triangulo_rectangulo(altura)
            except ValueError:
                print("Por favor, introduce un número entero válido.")
        
        elif opcion == '6':
            print("Saliendo del programa.Gracias por tu preferencia ¡Adiós!")
            break
        
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")

       
