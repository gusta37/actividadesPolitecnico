# Ejercicio estructura condicional simple:
# 1. Realice un programa que solicite dos letras ingresadas por el usuario y verifique si son iguales o no, mostrando un mensaje.
"""
letra1 = input("\nIngrese la primera letra: ")
letra2 = input("Ingrese la segunda letra: ")

if letra1 == letra2:
    print("\n👌 Las letras son iguales")
else:
    print("\n✖️ Las letras son diferentes")
"""

# Versión avanzada:
'''letras = []
for i in range (1, 3):
    while True:
        
        letra = input(f'Ingresá la letra {i}: ').strip().upper()
        if len(letra) == 1 and letra.isalpha():
            letras.append(letra)
            break
        else:
            print('Dato incorrecto. Debes ingresar una única letra.')
        
print(f'Ingresaste {letras[0]} y {letras[1]}.')    
print(f'{letras[0]} y {letras[1]} son iguales.' if letras[0] == letras[1] else f'{letras[0]} y {letras[1]} son diferentes.')'''
    
#2. Hacer un programa que permita decidir si dos palabras son iguales o diferentes. Mostrar mensaje por pantalla.
"""
palabra1 = input("\nIngrese la primera palabra: ")
palabra2 = input("\nIngrese la segunda palabra: ")

if palabra1 == palabra2:
    print("\n👌 Las palabras son iguales")
else:
    print("\n✖️ Las palabras son diferentes")
"""
#3. Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.
"""
genero = input("\nIngrese f para femenino o m para masculino: ")

if genero == "f":    
    print("\n👩‍♀️ Vota en mesa femenina")    
elif genero == "m":
    print("\n👨‍♂️ Vota en mesa masculina")
"""
#4. Realice un programa que lea dos números y diga cuál es el mayor.
"""
numero1 = int(input("\nIngrese el primer numero: "))
numero2 = int(input("\nIngrese el segundo numero: "))

if numero1 > numero2:
    print(f"\nEl numero {numero1} es mayor que {numero2}")
else:
    print(f"\nEl numero {numero2} es mayor que {numero1}")
"""
#5. Realice un programa que cambie pesos a dólares. Mejórelo, añadiendo el cambio de dólares a pesos y que sea el usuario quién decida qué tipo de cambio quiere, si de dólares a pesos o viceversa.

# Pesos a dólares original: 
"""
pesos = float(input("\nIngrese la cantidad de pesos: "))
valorDolar = 0.00096
pesoADolar = (pesos * valorDolar)

print(f"\n${pesos} pesos Argentinos son u$s{pesoADolar} dólares estadounidenses.")
"""
# Mejorado: 
"""
tipoCambio = input("\nIngrese el tipo de cambio que quiere realizar: \n 1-Pesos a dólares\n 2-Dólares a pesos: ")

if tipoCambio == "1":
    pesos = float(input("\nIngrese la cantidad de pesos: "))
    valorDolar = 0.00096
    pesoADolar = (pesos * valorDolar)
    print(f"\n${pesos} pesos Argentinos son u$s{pesoADolar} dólares estadounidenses.")
elif tipoCambio == "2":
    dolares = float(input("\nIngrese la cantidad de dólares: "))
    valorPeso = 1040.25
    dolarAPeso = (dolares * valorPeso)    
    print(f"\nu$s{dolares} dólares estadounidenses son ${dolarAPeso} pesos Argentinos.")
"""    

#6. Realice un programa donde el usuario ingrese su edad. Si es mayor de 16 años, muestre un mensaje diciendo “puede votar”, sino “no vota”.

edad = int(input("\nIngrese su edad: "))

if edad >= 16:
    print("\n👍 Puede votar")
else:
    print("\n👎 No puede votar aún")
