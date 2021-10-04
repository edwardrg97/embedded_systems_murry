import RPi.GPIO as GPIO
import telepot
import time
from telepot.loop import MessageLoop

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 27
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


bot = telepot.Bot('')


def getDistance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2
 
    return distance



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
    if command == 'start':
        bot.sendMessage(chatId, 'Checking your home!')
        while True:
            dist = getDistance()
            if dist < 20:
                bot.sendMessage(chatId, 'Someone is in your home!')
                time.sleep(2)
            #else: 
                #message = 'None in your home, distance ' + str(dist)
                #bot.sendMessage(chatId, message)
            #time.sleep(10)


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
