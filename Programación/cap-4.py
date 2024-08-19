""" 
CUADERNILLOS DE EJERCITACIÓN
Ejercicio estructura condicional simple:
1. Realice un programa que solicite dos letras ingresadas por el usuario y
verifique si son iguales o no, mostrando un mensaje.
"""

""" print("\nIngresá dos letras y veremos si son iguales...\n")

letra1 = input("Ingresa la primera letra: ")

# Verifico que el primer ingreso sea una letra
if not letra1.isalpha():
    print("\nError: Debes ingresar solo letras 🚫. Vuelve a intentarlo.")
else:
    letra2 = input("Ingresa la segunda letra: ")
    
    # Verifico que el segundo ingreso sea una letra
    if not letra2.isalpha():
        print("\nError: Debes ingresar solo letras 🚫. Vuelve a intentarlo.")
    else:
        # Convierto ambas letras a minúsculas para evitar conflicto por mayúsculas/minúsculas
        letra1 = letra1.lower()
        letra2 = letra2.lower()

        if letra1 == letra2:
            print("\nLas letras son iguales 👌")
        else:
            print("\nLas letras son diferentes ⚠️") """

"""
2. Hacer un programa que permita decidir si dos palabras son iguales o
diferentes. Mostrar mensaje por pantalla.
"""

""" print("\nIngresá dos palabras y veremos si son iguales o diferentes...\n")

palabra1 = input("Ingresa la primera palabra: ")
palabra2 = input("Ingresa la segunda palabra: ")

# Verifico que el primer ingreso sea una palabra

if not palabra1.isalpha():
    print("\nError: Debes ingresar solo palabras 🚫. Vuelve a intentarlo.")
else:
    # Verifico que el segundo ingreso sea una palabra
    if not palabra2.isalpha():
        print("\nError: Debes ingresar solo palabras 🚫. Vuelve a intentarlo.")
    else:
        # Convierto ambas palabras a minúsculas para evitar conflicto por mayúsculas/minúsculas
        palabra1 = palabra1.lower()
        palabra2 = palabra2.lower()

        if palabra1 == palabra2:
            print("\nLas palabras son iguales 👌")
        else:
            print("\nLas palabras son diferentes ⚠️") """

"""
3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota
en mesa femenina o masculina.
"""

""" print("\nIngresá 'f' o 'm' y veremos si vota en mesa femenina o masculina...\n")

genero = input("Ingresa 'f' o 'm': ")

# Verifico que el dato ingresado sea una letra

if not genero.isalpha():
    print("\nError: Debes ingresar solo 'f' o 'm' 🚫. Vuelve a intentarlo.")
else:
    genero = genero.lower()

    if genero == 'f':
        print("\nVota en mesa femenina 💁‍♀️")
    elif genero == 'm':
        print("\nVota en mesa masculina 💁‍♂️")
    else:
        print("\nError: Debes ingresar solo 'f' o 'm' 🚫. Vuelve a intentarlo.") """

"""
4. Realice un programa que lea dos números y diga cuál es el mayor.
"""

""" print("\nIngresá dos números y veremos cual es el mayor...\n")

num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))


if num1 > num2:
    print(f"\n{num1} es mayor que {num2}") # Usar format f-string!!!
elif num1 < num2:
    print(f"\n{num2} es mayor que {num1}")
else:
    print(f"\n{num1} y {num2} son iguales") """

"""
5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo
el cambio de dólares a pesos y que sea el usuario quién decida qué tipo
de cambio quiere, si de dólares a pesos o viceversa.
"""

""" print("\n¿Qué tipo de cambio quieres?\n")

tipoCambio = int(input("1-Dolares a Pesos\n2-Pesos a Dolares\n"))

if tipoCambio == 1:
    dolares = float(input("\nIngresa la cantidad de dolares: u$s "))
    dolaresAPesos = dolares * 943.28 # 1 dolar = 943.28 pesos argentinos al 19/8/24.
    print(f"\nu$s{dolares:.2f} dolares equivalen a ${dolaresAPesos:.2f} pesos")
elif tipoCambio == 2:
    pesos = float(input("\nIngresa la cantidad de pesos: $ "))
    pesosADolares = pesos / 943.28
    print(f"\n${pesos:.2f} pesos equivalen a u$s{pesosADolares:.2f} dolares")
else:
    print("\nError: Debes ingresar solo 1 o 2 🚫. Vuelve a intentarlo.") """

"""
6. Realice un programa donde el usuario ingrese su edad. Si es mayor de
16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.
"""

print("\nBienvenido a las mesas de votaciones.\n\nIngresá tu edad")

edad = int(input())

if edad >= 16:
    print("\nPuedes votar.")
else:
    print("\nAun no puedes votar 🚫10. Debes ser mayor de 16 años.")