#Ejercicios estructuras repetitivas y estructuras condicionales.
#1. Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.

# Solicitar 4 números al usuario
"""numeros = []
for i in range(1, 5):
    numero = int(input(f"Ingrese el número {i}: "))
    numeros.append(numero)

# Inicializar contadores y sumatorias
contador_pares = 0
contador_impares = 0
sumatoria_pares = 0

# Procesar los números
for numero in numeros:
    if numero % 2 == 0:
        contador_pares += 1
        sumatoria_pares += numero
    else:
        contador_impares += 1

# Resultados
print(f"\nLa cantidad de números pares es: {contador_pares}")
print(f"La cantidad de números impares es: {contador_impares}")
print(f"La sumatoria de los números pares es: {sumatoria_pares}")"""


#2. Leer 10 números y obtener la cantidad de mayorEdad y la cantidad de menorEdad a 100, cuál es el número máximo y cuál es el número mínimo.

"""# Inicialización de variables
numeros = []
mayorEdad_100 = 0
menorEdad_100 = 0
maximo = None
minimo = None

# Leer los números del usuario
for i in range(1, 11):  # Cambia 11 por la cantidad de números deseada
    numero = int(input(f"Ingrese el número {i}: "))
    numeros.append(numero)

    # Contar mayorEdad y menorEdad a 100
    if numero > 100:
        mayorEdad_100 += 1
    else:
        menorEdad_100 += 1

    # Actualizar máximo y mínimo
    if maximo is None or numero > maximo:
        maximo = numero
    if minimo is None or numero < minimo:
        minimo = numero

# Mostrar los resultados
print("\nResultados:")
print(f"- La cantidad de números mayorEdad a 100 es: {mayorEdad_100}")
print(f"- La cantidad de números menorEdad o iguales a 100 es: {menorEdad_100}")
print(f"- El número más grande es: {maximo}")
print(f"- El número más pequeño es: {minimo}")"""


#3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, cuántos varones, cuántos mayorEdad de edad y cuántos menorEdad de edad.

"""# Inicializar contadores
mujeres = 0
varones = 0
mayorEdad = 0
menorEdad = 0

# Leer datos para 15 personas
for i in range(1, 16):  # Desde 1 hasta 15
    print(f"\nPersona {i}:")
    
    # Pedir la edad
    edad = int(input("Ingrese la edad: "))
    
    # Pedir el sexo y validar
    while True:
        sexo = input("Ingrese el sexo (F para mujer, M para varón): ").upper()
        if sexo in ['F', 'M']:
            break
        else:
            print("Sexo no válido. Por favor ingrese 'F' o 'M'.")

    # Actualizar contadores según el sexo
    if sexo == 'F':
        mujeres += 1
    elif sexo == 'M':
        varones += 1

    # Actualizar contadores según la edad
    if edad >= 18:
        mayorEdad += 1
    else:
        menorEdad += 1

# Mostrar resultados
print("\nResultados finales:")
print(f"- Cantidad de mujeres: {mujeres}")
print(f"- Cantidad de varones: {varones}")
print(f"- Cantidad de mayores de edad: {mayorEdad}")
print(f"- Cantidad de menores de edad: {menorEdad}")"""


#4. Leer 10 números y mostrar solamente los números positivos, y su sumatoria.

"""numeros = [] 
numerosPositivos = []
numerosNegativos = []
sumatoriaPositivos = 0
sumatoriaNegativos = 0

for i in range(1,11):
    numero = int(input(f"Ingrese el número {i}: "))
    numeros.append(numero)
    if numero > 0:
        numerosPositivos.append(numero)
        sumatoriaPositivos += numero
    elif numero < 0:
        numerosNegativos.append(numero) 
        sumatoriaNegativos += numero
    else:
        print(f"El número {i} es cero, que no es positivo ni negativo.")


print(f"\nTodos los números son: {numeros}")
print(f"\nLos números positivos son: {numerosPositivos}")
print(f"\nLos números negativos son: {numerosNegativos}")
print(f"\nLa sumatoria de los números positivos es: {sumatoriaPositivos}")
print(f"\nLa sumatoria de los números negativos es: {sumatoriaNegativos}")"""

#5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.

numerosNegativos = []

for i in range(1,16):
    numero = int(input(f"Ingrese el número {i}: "))
    numerosNegativos.append(numero)

valoresAbsolutos = [abs(num) for num in numerosNegativos]
# abs muestra el valor absoluto sin los signos.

print(f"\nLos valores absolutos de estos números son: {valoresAbsolutos}")