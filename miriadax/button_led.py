import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

button = 18
GPIO.setup(button,GPIO.IN,pull_up_down=GPIO.PUD_UP)

led = 21
GPIO.setup(led,GPIO.OUT)

while True:
    input_state = GPIO.input(button)
    if input_state == False:
        print('Button Pressed')
        GPIO.output(led,1)
        time.sleep(0.2)
    else:
        GPIO.output(led,0)
