from gpiozero import LEDBoard,Button
from time import sleep

leds = LEDBoard(5,6,13)
boton = Button(2)
n=0
while True:
    while n==0 and boton.is_pressed == 0:
        leds.value = (1,0,0)
        sleep(5)
        x=5
        while (x > 0 and boton.is_pressed == 0):
            leds.value = (0,1,0)
            sleep(1)
            leds.value = (0,0,0)
            sleep(1)
            x = x - 1
        leds.value = (0,0,1)
        sleep(5)
        x=5
        while (x > 0 and boton.is_pressed == 0):
            leds.value = (0,0,1)
            sleep(1)
            leds.value = (0,0,1)
            sleep(1)
            x = x - 1 
    else:
        print("interruption")
        leds.value = (0,0,1)
        sleep(5)

