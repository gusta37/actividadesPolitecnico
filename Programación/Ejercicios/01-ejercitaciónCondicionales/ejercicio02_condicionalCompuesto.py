# Ejercicios estructura condicional compuesto (IF anidados)
#1. Introducir los lados de un triángulo y visualizar por pantalla si dicho triángulo es equilátero, isósceles o escaleno.
"""
lado1 = int(input("\nIngrese el primer lado: "))
lado2 = int(input("Ingrese el segundo lado: "))
lado3 = int(input("Ingrese el tercer lado: "))

if lado1 == lado2 and lado2 == lado3:#todo son iguales
    print("\n👌 El triángulo es equilátero")
    
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:#al menos dos son iguales. 
    print("\n👌 El triángulo es isósceles")
else:
    print("\n👌 El triángulo es escaleno")
"""

"""2. Realice un programa que le permita al usuario simular el pago ingresando el importe y la forma de pago:
• Contado (1): se aplica un descuento del 10% al importe
• Tarjeta (2): se aplica un interés de 10%
• Débito (3): se aplica un descuento del 5%
Mostrar el importe, el descuento o interés y el importe total."""

"""tipoPago = int(input("\nIngrese el tipo de pago: \n 1-Contado: se aplica un descuento del 10% al importe. \n 2-Tarjeta: se aplica un interés de 10%. \n 3-Débito: se aplica un descuento del 5% \n"))

if tipoPago == 1:
    importe = float(input("\nIngrese el importe: "))
    descuento = importe * 0.1
    importeTotal = importe - descuento
    print(f"\nEl importe es: ${importe} \nEl descuento es: ${descuento} \nEl importe total es: ${importeTotal}")    
elif tipoPago == 2:
    importe = float(input("\nIngrese el importe: "))
    interes = importe * 0.1
    importeTotal = importe + interes
    print(f"\nEl importe es: ${importe} \nEl interés es: ${interes} \nEl importe total es: ${importeTotal}")
elif tipoPago == 3:
    importe = float(input("\nIngrese el importe: "))
    descuento = importe * 0.05
    importeTotal = importe - descuento
    print(f"\nEl importe es: ${importe} \nEl descuento es: ${descuento} \nEl importe total es: ${importeTotal}")"""

#3. Realice un programa que lea tres números, muestre cuál es el mayor y determine si es par o impar.

"""numero1 = int(input("\nIngrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))

if numero1 > numero2 and numero1 > numero3: 
    print(f"\nEl número {numero1} es el mayor")
    if numero1 % 2 == 0:
        print(f"\nEl número {numero1} es par")
    else:
        print(f"\nEl número {numero1} es impar")
elif numero2 > numero1 and numero2 > numero3: 
    print(f"\nEl número {numero2} es el mayor")
    if numero2 % 2 == 0:
        print(f"\nEl número {numero2} es par")
    else:
        print(f"\nEl número {numero2} es impar")
else:
    print(f"\nEl número {numero3} es el mayor")
    if numero3 % 2 == 0:
        print(f"\nEl número {numero3} es par")
    else:
        print(f"\nEl número {numero3} es impar")  """  

#4. Confeccione un programa que pida un número del 1 al 7 y diga el día de la semana correspondiente.

"""numeroSemana = int(input("\nIngrese un número del 1 al 7: "))

if numeroSemana == 1:
    print("\n👌 Hoy es Lunes")    
elif numeroSemana == 2:
    print("\n👌 Hoy es Martes")    
elif numeroSemana == 3:
    print("\n👌 Hoy es Miercoles")    
elif numeroSemana == 4:
    print("\n👌 Hoy es Jueves")    
elif numeroSemana == 5:
    print("\n👌 Hoy es Viernes")    
elif numeroSemana == 6:
    print("\n👌 Hoy es Sabado")    
elif numeroSemana == 7:
    print("\n👌 Hoy es Domingo")    
else:
    print("\n✖️ El número ingresado no es válido")"""

#5. Realice un programa que pida un número del 1 al 12 y diga el nombre del mes correspondiente.

numeroMes = int(input("\nIngrese un número del 1 al 12: "))

if numeroMes == 1:
    print("\n👌 Enero")    
elif numeroMes == 2:
    print("\n👌 Febrero")    
elif numeroMes == 3:
    print("\n👌 Marzo")    
elif numeroMes == 4:
    print("\n👌 Abril")    
elif numeroMes == 5:
    print("\n👌 Mayo")    
elif numeroMes == 6:    
    print("\n👌 Junio")    
elif numeroMes == 7:
    print("\n👌 Julio")    
elif numeroMes == 8:
    print("\n👌 Agosto")            
elif numeroMes == 9:
    print("\n👌 Septiembre")            
elif numeroMes == 10:
    print("\n👌 Octubre")            
elif numeroMes == 11:
    print("\n👌 Noviembre")            
elif numeroMes == 12:
    print("\n👌 Diciembre")            
else:
    print("\n✖️ El número ingresado no es válido")