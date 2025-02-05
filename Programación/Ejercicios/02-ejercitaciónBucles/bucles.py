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

# version sin contadores. solo listas y metodos de python: tambien agrego excepcion que verifique que se esta ingresando solo numeros!

# 1. Realice un programa que lea 4 números y diga cuántos son pares y cuantos impares y devuelva la sumatoria de los pares.
'''numeros = []
paresList = []
imparesList = []

for i in range (1, 5):
    
    while True:
        try: # genera una excepcion generando un valueError: Uso de un bloque try-except para manejar errores si el usuario no ingresa un número entero.
            numero = int(input(f'Ingresá el número {i}: '))
            numeros.append(numero)
            break
        except ValueError: # No puedo usar una variable en el mensaje pq si falla ya no queda definida.
            print(f'Ingresaste un valor no válido y debe ser un número. Intentá de nuevo.')
            
# Filtrar los pares
paresList = [num for num in numeros if num % 2 == 0]

# Derivar los impares a partir de los pares
imparesList = [num for num in numeros if num not in paresList]

# Cálculos necesarios
sumPares = sum(paresList)
cantidadPares = len(paresList)
sumImpares = sum(imparesList)
cantidadImpares = len(imparesList)
            
print('\nLista completa de números: ')
print('*'*50)
for i, numero in enumerate(numeros):
    print(f'Número {i+1}: {numero}.')
print('*'*50)

print(f'\nHay {cantidadPares} números pares: {", ".join(map(str, paresList))} y {cantidadImpares} números impares: {", ".join(map(str, imparesList))}')
# lista de numeros dentro del string: map(str, paresList): Convierte cada número de la lista paresList en una cadena.
# ", ".join(...): Une todas las cadenas resultantes con una coma y un espacio entre ellas.
print(f'Todos los pares suman: {sumPares}.')'''    

#2. Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100 y cuál es el número máximo y cuál es el número mínimo.
'''# Pedir los 10 números:
numeros = []

for i in range(1,11):
    numero = int(input(f'Ingresá el número {i}: '))
    numeros.append(numero)

# listas:
mayorCienList = []
menorCienList = []

# contadores:
mayorCien = 0
menorCien = 0

# Máximo y minimo:
maximo = max(numeros)
minimo = min(numeros)

for numero in numeros:
    if numero > 100:
        mayorCienList.append(numero)
        mayorCien += 1 
    else:
        menorCienList.append(numero)
        menorCien += 1
        
print(f'Tus números son: {numeros}.')
print(f'Los números mayores a 100 son: {mayorCienList} y son {mayorCien} números.')
print(f'Los números menores a 100 son: {menorCienList} y son {menorCien} números.')
print(f'El número Máximo es {maximo} y el número mínimo es {minimo}.')'''

#version sin contadores: 
#2. Leer 10 números y obtener la cantidad de mayores y la cantidad de menores a 100 y 
#cuál es el número máximo y cuál es el número mínimo.
'''numeros = []
mayoresCien = []

for i in range (1, 5):

    while True:
        try:
            numero = int(input(f'Ingresa el número {i}: '))
            numeros.append(numero)
            break
        except ValueError:
            print('Ingresaste un valor que no es válido, debe ser un número. Intenta de nuevo.')
            
# Filtramos los mayores de 100 de la lista de los numeros:
mayoresCien = [num for num in numeros if num > 100]

# Derivamos los menores de 100 de la lista d numeros:
menoresCien = [num for num in numeros if num not in mayoresCien]

# cálculos:
cantidadMayores = len(mayoresCien)
cantidadMenores = len(menoresCien)
numeroMaximo = max(numeros)
numeroMinimo = min(numeros)

print(f'Ingresaste los números: {", ".join(map(str, numeros))}.')
print(f'Hay {cantidadMayores} números mayores de 100: {", ".join(map(str, mayoresCien))} y {cantidadMenores} menores: {", ".join(map(str, menoresCien))}.')
print(f'El número más grande es {numeroMaximo} y es menor es {numeroMinimo}.')'''

#Ejercicios estructuras repetitivas y estructuras condicionales.
'''#3. Ingresar las edades y el sexo de 15 personas y determinar cuántas son mujeres, 
cuántos varones, cuántos mayores de edad y cuántos menores de edad.
personas = []

# contadores:
hombres = 0
mujeres = 0
mayores = 0 
menores = 0

for i in range (1, 5):
    edad = int(input(f'Ingresá la edad de la persona {i}: '))
    
    # Validación del sexo. Uso While pq me permite volver a pedir el sexo si se ingresa un dato incorrecto. Solo funciona el break si el dato es correcto y recien pasa a la otra persona.
    while True:
        sexo = input(f'Ingresá el sexo de la persona {i} (F para mujer y M para varón): ').strip().upper()
        if sexo in ['F', 'M']:
            break
        else:
            print('Sexo no válido. Por favor, ingresa "F" para mujer o "M" para varón.')

    
    # Guardar los datos en la lista
    personas.append({'edad': edad, 'sexo': sexo})
    
    # cuantos mujeres y cuantos hombres:
    
    if sexo == 'F':
        mujeres += 1
    else:
        hombres += 1
        
    if edad >= 18:
        mayores += 1
    else:
        menores += 1

print('Listado de Personas:')
print('-'*50)
for i, persona in enumerate(personas, start=1):
    print(f"Persona {i}: Edad: {persona['edad']}, Sexo: {'Mujer' if persona['sexo']== 'F' else 'Hombre'}")
    print('-'*50)
print(f'Hay {mujeres} mujeres y {hombres} hombres.')
print(f'{mayores} son mayores y {menores} son menores.')'''

#4. Leer 10 números y mostrar solamente los números positivos, y su sumatoria.'''
'''numeros = []
numPositivos = []

for i in range (1, 11):
    numero = int(input(f'Ingresá el número {i}: '))
    numeros.append(numero)
    
    numPositivos.append(numero) if numero >= 0 else 0
 
sumPositivos = sum(numPositivos)  

print(f'Lista de todos los numeros: ')
print('*'*30)
for i, numero in enumerate(numeros):
    print(f'Número {i+1}: {numero}.')
print('*'*30)
print(f'Los números positivos son {numPositivos} y suman en total {sumPositivos}.')
print('*'*30)'''

#5. Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
'''numerosNegativos = []

for i in range (1, 16):
    while True:
        numeroNegativo = int(input(f'Ingresá el número negativo número {i}: '))
        if numeroNegativo <= 0:
            numerosNegativos.append(numeroNegativo)
            break
        else:
            print(f'Ingresaste {numeroNegativo} y no es un número negativo. Intentá de nuevo.\n')
            
    # Mostrar el valor absoluto sin el signo menos:
    volarAbsoluto = [abs(numeroNegativo) for numeroNegativo in numerosNegativos]
            
print('\nLista de números negativos ingresados: ')
print('*'*40)
for i, numeroNegativo in enumerate(numerosNegativos):
    print(f'Número {i+1}: {numeroNegativo}.')
print('*'*40)

print('\nLista de números convertidos en positivos: ')
print('*'*40)
for i, valor in enumerate(volarAbsoluto):
    print(f'Número {i+1}: {valor}.')
print('*'*40)'''
