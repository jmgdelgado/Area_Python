#!/usr/bin/python
import RPi.GPIO as GPIO                  # Import GPIO library
from gpiozero import LightSensor, LED    # Import gpiozero library
import Adafruit_BMP.BMP085 as BMP085     # Import library for Barometric sensor
import Adafruit_DHT                      # Library for temperature humiditi sensor
import json
import time 
from mysensores import carriots

# Sensor: Photoresistor
ldr = LightSensor(6)    # Photoresistor in pin 6

print('Sensor: Photoresistor GL5516')
print('   Intensidad luminica = {0:0.2f} %'.format(ldr.value))
# Obteniendo los datos en la variables para enviar a Carriots
photores = ldr.value

# Sensor: BMP180 
sensor = BMP085.BMP085()

print ('Sensor: BMP180')
print ('   Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
print ('   Presion = {0:0.2f} Pa'.format(sensor.read_pressure()))
print ('   Altitud = {0:0.2f} *C'.format(sensor.read_altitude()))
print ('   Sealevel Pressure = {0:0.2f} *C'.format(sensor.read_sealevel_pressure()))

# Obteniendo los datos en la variables para enviar a Carriots
bmp_temp = sensor.read_temperature()
bmp_press = sensor.read_pressure()
bmp_alt = sensor.read_altitude()

# Sensor: DHT11
humidity, temperature = Adafruit_DHT.read_retry(11,4)
print ('Sensor: DHT11')
print ('   Temp: {0:0.1f} C '.format(temperature))
print ('   Humidity: {0:0.1f} %'.format(humidity))
#print ('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature,humidity))
# Obteniendo los datos en la variables para enviar a Carriots
dht_temp = temperature
dht_humid = humidity

# Sensor: Sensor de lluvia. Rain sensor
GPIO.setmode(GPIO.BCM)
entrada_sensor = 12
GPIO.setup(entrada_sensor,GPIO.IN)

input_state = GPIO.input(entrada_sensor)
if input_state == False:
        estado_lluvia = 'Lluvia'
else:
        estado_lluvia = 'Seco'

print ('Sensor: Rain sensor')
print ('   Estado: ', estado_lluvia)


# POST para guardar los datos en Carriots

datos = dict(
                  ligth=photores,
                  BMP_temp=bmp_temp,
                  BMP_press=bmp_press,
                  BMP_alt=bmp_alt,
                  DHT_temp=dht_temp,
                  DHT_humid=dht_humid,
                  lluvia=estado_lluvia)

f = carriots.postDataCarriots(datos) 


#Print in a pretty way
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
    

