import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

entrada_sensor = 12

GPIO.setup(entrada_sensor,GPIO.IN)

while True:
    input_state = GPIO.input(entrada_sensor)
    if input_state == False:
        print('Lluvia')
        time.sleep(0.8)
    else:
        print('Seco')
        time.sleep(0.8)
        
