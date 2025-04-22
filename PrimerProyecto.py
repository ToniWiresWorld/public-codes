from machine import Pin
from time import sleep

led = Pin(1, Pin.OUT)  # En esta placa el PIN1 es el LED interno.

while True:
    led.value(not led.value())
    sleep(0.5)
