from gpiozero import LightSensor, LED
import time

ldr = LightSensor(18)

led = LED(21)

while True:
    print("valor: ")
    print(ldr.value)
    print("nivel: ")
    print(ldr.threshold)
    if ldr.value > ldr.threshold:
        led.off()
        print("light")
    else:
        led.on()
        print("dark")
    time.sleep(0.5)
        
