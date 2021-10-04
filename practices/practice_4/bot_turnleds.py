import RPi.GPIO as GPIO
import time
import telepot
from telepot.loop import MessageLoop

GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)
bot = telepot.Bot('2008128052:AAHB68zl15lodsB4HAYTCVkXmCDiciEJelw')

#Turn on and off functions
def turnOn(chatId):
    GPIO.output(LED_PIN, True)
    bot.sendMessage(chatId, 'The led is ON now!')

def turnOff(chatId):
    GPIO.output(LED_PIN, False)
    bot.sendMessage(chatId, 'The led is OFF now!')

#Main bot function
def handleCommand(msg):
    contentType, chatType, chatId = telepot.glance(msg) 
    print(contentType, chatType, chatId)

    #Cheking command with the "separator"
    if contentType != 'text':
        return 
    message = msg['text']

    if not message.startswith('!'):
        return
    
    #Call previous functions
    command = message[1:].lower() 
    if command == 'on':
        turnOn(chatId)
    elif command == 'off':
        turnOff(chatId)

if __name__ == '__main__':
    try:
        MessageLoop(bot, handleCommand).run_as_thread()

        while 1:
            time.sleep(10)
    except KeyboardInterrupt:
        print("Intrerrupted by user")
        pass
    finally:
        print("Program stopped")
        GPIO.cleanup()