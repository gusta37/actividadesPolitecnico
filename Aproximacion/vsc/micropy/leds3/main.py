# Primero llamo los módulos a trabajar:

from machine import Pin
from utime import sleep

# Se crean los Objetos:

led_verde = Pin(15, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
led_rojo = Pin(4, Pin.OUT)

# Comenzar el ciclo de código.

while True:
    
    led_verde.value(1)
    print("On")
    sleep(1)
    led_verde.value(0)
    print("Off")
    sleep(1)

    led_amarillo.value(1)
    print("On")
    sleep(1)
    led_amarillo.value(0)
    print("Off")
    sleep(1)

    led_rojo.value(1)
    print("On")
    sleep(1)
    led_rojo.value(0)
    print("Off")
    sleep(1)