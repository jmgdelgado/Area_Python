"""
Sensor de lluvia
Se conecta la placa detectora de lluvia al microcircuito sin cruzar los cables
El microcontrolador tiene una salida analogica A0 que no vamos a utilizar
Se conecta el pin VCC del controlador a 5V
Se conecta el pin _GND a tierra 
Se conecta el pin D0 (salida digital) a la entrada GPIO que queramos
"""

import RPi.GPIO as GPIO                  # Import GPIO library


def llueve (pin_datos):        # Creo una funcion para obtener la intensidad luminica
    result = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_datos,GPIO.IN)
    
    input_state = GPIO.input(pin_datos) 
    result = input_state
 
    return  result      # devuelvo la lectura
    

if __name__ == '__main__':
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
