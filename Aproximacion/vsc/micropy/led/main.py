# Primero llamo los módulos a trabajar:

from machine import Pin
from utime import sleep

# Segundo se crea el objeto: 
# Led:

led_rojo = Pin(2, Pin.OUT)

# Desarrollando el ciclo y el codigo:

while True:
    led_rojo.value(1)
    sleep(2)
    print("on")
    led_rojo.value(0)
    sleep(2)
    print("off")