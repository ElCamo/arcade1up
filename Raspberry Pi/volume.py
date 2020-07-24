import RPi.GPIO as GPIO
from time import sleep
from subprocess import call

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

volumeState = 0

while True:
        buttonState1 = GPIO.input(16)
        buttonState2 = GPIO.input(12)

        if buttonState1 == False and buttonState2 == False and volumeState != 96:
                print("Switch was set to Vol HIGH")
                print(volumeState)
                call(["amixer", "set", "Headphone", "96%"])
                volumeState = 96
                sleep(1)

        if buttonState1 == True and buttonState2 == True and volumeState != 0:
                print("Switch was set to Vol ZERO")
                print(volumeState)
                call(["amixer", "set", "Headphone", "0%"])
                volumeState = 0
                sleep(1)

        if buttonState1 == False and buttonState2 == True and volumeState != 50:
                print("Switch was set to Vol LOW")
                print(volumeState)
                call(["amixer", "set", "Headphone", "unmute"])
                call(["amixer", "set", "Headphone", "85%"])
                volumeState = 50
                sleep(1)
