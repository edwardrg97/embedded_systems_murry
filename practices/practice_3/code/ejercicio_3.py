from bluedot import BlueDot
from gpiozero import PWMLED
from signal import pause

def set_brightness(pos):
	brightness = (pos.y + 1) / 2
	
	if brightness > 0.6:
		print("Verde")
		led1.value = brightness
		led2.value = 0
		led3.value = 0
		
	elif brightness >= 0.3 and brightness <= 0.6:
		print("Amarillo")
		led1.value = 0
		led2.value = brightness
		led3.value = 0 
			
	elif brightness < 0.3:
		print("Rojo")
		led1.value = 0
		led2.value = 0
		led3.value = brightness 	
	print(brightness)

led1 = PWMLED(17)	
led2 = PWMLED(27)
led3 = PWMLED(22)

led1.value = 1
bd = BlueDot()
bd.when_moved = set_brightness
pause()
