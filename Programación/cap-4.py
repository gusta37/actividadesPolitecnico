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

""" print("\nBienvenido a las mesas de votaciones.\n\nIngresá tu edad")

edad = int(input())

if edad >= 16:
    print("\nPuedes votar.")
else:
    print("\nAun no puedes votar 🚫10. Debes ser mayor de 16 años.") """

""" Ejercicios estructura condicional compuesto (IF anidados)
1. Introducir los lados de un triángulo y visualizar por pantalla si dicho
triángulo es equilátero, isósceles o escaleno.
Equilátero: tres lados iguales.
Isósceles: dos lados iguales.
Escaleno: tres lados diferentes.
"""
"""
print("\nIngresá los tres lados de un triángulo y veremos si es equilátero, isósceles o escaleno...\n")

lado1 = int(input("Ingresa el primer lado: "))
lado2 = int(input("Ingresa el segundo lado: "))
lado3 = int(input("Ingresa el tercer lado: "))

if lado1 == lado2 == lado3:
    print("\nTu triángulo es Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("\nTu triángulo es Isósceles")
else:
    print("\nTu triángulo es Escaleno") """

"""
2. Realice un programa que le permita al usuario simular el pago
ingresando el importe y la forma de pago:
• Contado (1): se aplica un descuento del 10% al importe
• Tarjeta (2): se aplica un interés de 10%
• Débito (3): se aplica un descuento del 5%
Mostrar el importe, el descuento o interés y el importe total."""

""" monto = float(input("\nIngresa el monto que querés pagar: $ "))
formaPago = int(input("\nIngresa la forma de pago\n\n1-Contado\n2-Tarjeta\n3-Debito\n"))

if formaPago == 1: # Contado
    descuento = monto * 0.10 # multiplacando por 0.10 obtenemos el 10% del monto
    montoTotal = monto - descuento
    print(f"\nEl importe que deseas abonar es de: ${monto:.2f}\nComo abonás al CONTADO, se aplica un Descuento de: ${descuento:.2f} (el 10%)\nEl monto total a pagar es: ${montoTotal:.2f}")
elif formaPago == 2: # Tarjeta
    interés = monto * 0.10
    montoTotal = monto + interés
    print(f"\nEl importe que deseas abonar es de: ${monto:.2f}\nComo abonás con TARJETA, se aplica un interés de: ${interés:.2f} (el 10%)\nEl monto total a pagar es: ${montoTotal:.2f}")
elif formaPago == 3: # Debito
    descuento = monto * 0.05
    montoTotal = monto - descuento
    print(f"\nEl importe que deseas abonar es de: ${monto:.2f}\nComo abonás con DÉBITO, se aplica un Descuento de: ${descuento:.2f} (el %5)\nEl monto total a pagar es: ${montoTotal:.2f}")
else:
    print("\nError: Debes ingresar solo 1, 2 o 3 🚫. Vuelve a intentarlo.") """

"""
3. Realice un programa que lea tres números, muestre cuál es el mayor y
determine si es par o impar."""

""" num1 = int(input("\nIngresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
num3 = int(input("Ingresa el tercer número: "))

if num1 > num2 and num1 > num3:

    print(f"\n{num1} es el Mayor de los números.")
    if num1 % 2 == 0:
        print(f"\n{num1} es par.")
    else:
        print(f"\n{num1} es impar.")

elif num2 > num1 and num2 > num3:

    print(f"\n{num2} es el Mayor de los números.")
    if num2 % 2 == 0:
        print(f"\n{num2} es par.")
    else:
        print(f"\n{num2} es impar.")

else:

    print(f"\n{num3} es el Mayor de los números.")
    if num3 % 2 == 0:
        print(f"\n{num3} es par.")
    else:
        print(f"\n{num3} es impar.") """
      
"""
4. Confeccione un programa que pida un número del 1 al 7 y diga el día de
la semana correspondiente."""

""" numero = int(input("\nIngresa un número del 1 al 7: "))

if numero == 1:
    print("\nHoy es Lunes.")
elif numero == 2:
    print("\nHoy es Martes.")
elif numero == 3:
    print("\nHoy es Miercoles.")
elif numero == 4:
    print("\nHoy es Jueves.")
elif numero == 5:
    print("\nHoy es Viernes.")
elif numero == 6:
    print("\nHoy es Sabado.")
elif numero == 7:
    print("\nHoy es Domingo.")
else:
    print("\nError: Debes ingresar solo 1, 2, 3, 4, 5, 6 o 7 🚫. Vuelve a intentarlo.") """

"""
5. Realice un programa que pida un número del 1 al 12 y diga el nombre
del mes correspondiente. """

""" numero = int(input("\nIngresa un número del 1 al 12: "))

if numero == 1:
    print(f"\n{numero} es el mes de Enero.")
elif numero == 2:
    print(f"\n{numero} es el mes de Febrero.")
elif numero == 3:
    print(f"\n{numero} es el mes de Marzo.")
elif numero == 4:
    print(f"\n{numero} es el mes de Abril.")
elif numero == 5:
    print(f"\n{numero} es el mes de Mayo.")
elif numero == 6:
    print(f"\n{numero} es el mes de Junio.")
elif numero == 7:
    print(f"\n{numero} es el mes de Julio.")
elif numero == 8:
    print(f"\n{numero} es el mes de Agosto.")
elif numero == 9:
    print(f"\n{numero} es el mes de Septiembre.")
elif numero == 10:
    print(f"\n{numero} es el mes de Octubre.")
elif numero == 11:
    print(f"\n{numero} es el mes de Noviembre.")
elif numero == 12:
    print(f"\n{numero} es el mes de Diciembre.")
else:
    print("\nError: Debes ingresar solo 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 o 12 🚫. Vuelve a intentarlo.") """


