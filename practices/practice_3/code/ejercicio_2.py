#Construya un semáforo peatonal utilizando sus leds y 
#protoboard, dicho semáforo debe cambiar cuando se presione el BlueDot.
from bluedot import BlueDot
from signal import pause
from gpiozero import LEDBoard
leds = LEDBoard(17,27,22)

def state(pos):
	
	dimnValue = (pos.y + 1) / 2
	if dimnValue > 0.6:
		print("Verde")
		leds.value = (1,0,0)
	elif dimnValue >= 0.4 and dimnValue <= 0.6:
		print("Amarillo")
		leds.value = (0,1,0)
	elif dimnValue < 0.4:
		print("Rojo")
		leds.value = (0,0,1)
	print(dimnValue)


leds.value = (1,0,0)
bd = BlueDot()
bd.when_pressed = state
pause()
