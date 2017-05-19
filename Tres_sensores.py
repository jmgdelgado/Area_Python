#!/usr/bin/python
from gpiozero import LightSensor, LED
import Adafruit_BMP.BMP085 as BMP085
import Adafruit_DHT
#import sys

# Sensor: Photoresistor
ldr = LightSensor(6)

print('Sensor: Photoresistor GL5516')
print('   Intensidad luminica = {0:0.2f} %'.format(ldr.value))

# Sensor: BMP180 
sensor = BMP085.BMP085()

print ('Sensor: BMP180')
print ('   Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
print ('   Presion = {0:0.2f} Pa'.format(sensor.read_pressure()))
print ('   Altitud = {0:0.2f} *C'.format(sensor.read_altitude()))
print ('   Sealevel Pressure = {0:0.2f} *C'.format(sensor.read_sealevel_pressure()))

# Sensor: DHT11
humidity, temperature = Adafruit_DHT.read_retry(11,4)
print ('Sensor: DHT11')
print ('   Temp: {0:0.1f} C '.format(temperature))
print ('   Humidity: {0:0.1f} %'.format(humidity))
#print ('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature,humidity))
