#!/usr/bin/python
import RPi.GPIO as GPIO                  # Import GPIO library
import json
import time 
from mysensores import carriots         # Funciones para enviar y obtener datos de Carriots (almacenamiento Cloud)
from mysensores import DHT11            # Sensor de temperatura y humedad DHT11
from mysensores import BMP180           # Sensor barometrico BMP180, obtiene temperatura, presion y altitud
from mysensores import photoresistorGL5516  # Photoresistor para saber la intensidad luminica
from mysensores import sensorLluvia     # Sensor de lluvia, devuelve si llueve o no

# Sensor: Photoresistor
pin_photosensor = 6    # Photoresistor in pin 6
# Obteniendo los datos en la variables para enviar a Carriots
photores = photoresistorGL5516.luminosidad(pin_photosensor)

print('Sensor: Photoresistor GL5516')
print('   Intensidad luminica = {0:0.2f} %'.format(photores))


# Sensor: BMP180 
# Obteniendo los datos en la variables para enviar a Carriots
bmp_temp = BMP180.temperatura()
bmp_press = BMP180.presion()
bmp_alt = BMP180.altitud()
bmp_sl_press = BMP180.presion_nivel_mar()

print ('Sensor: BMP180')
print ('   Temp = {0:0.2f} *C'.format(bmp_temp))
print ('   Presion = {0:0.2f} Pa'.format(bmp_press))
print ('   Altitud = {0:0.2f} *C'.format(bmp_alt))
print ('   Sealevel Pressure = {0:0.2f} *C'.format(bmp_sl_press))


# Sensor: DHT11
pin_dht = 4
# dht_humid = DHT11.humidity(pin_dht)
# dht_temp = DHT11.temperature(pin_dht)
dht_humid,dht_temp = DHT11.datos_hum_temp(pin_dht)

print ('Sensor: DHT11')
print ('   Temp: {0:0.1f} C '.format(dht_temp))
print ('   Humidity: {0:0.1f} %'.format(dht_humid))
#print ('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature,humidity))


# Sensor: Sensor de lluvia. Rain sensor
entrada_sensor = 12

input_state = sensorLluvia.llueve(entrada_sensor)

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


# Respuesta a la peticion de POST. Print in a pretty way
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
    

