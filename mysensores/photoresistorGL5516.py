"""
Photoresistor GL5516
La salida del photoresistor es analogica, por ello hay que poner un capacitor
Se conecta una pata del photo resistor a 3.3V
Se conecta la otra pata del photo resistor con el positivo del condensador
Se conecta la entrada GPIO con el punto comun del photoresistor y el condensador
La pata negativa del condensador se conecta a tierra. El condensador es de 1 microfaradio 50V
"""

from gpiozero import LightSensor, LED    # Import gpiozero library



def luminosidad (pin_datos):        # Creo una funcion para obtener la intensidad luminica
    result = 0
    ldr = LightSensor(pin_datos)    
    # Si tengo resultado
    if ldr :      
        result = ldr.value
    else:
        print('Oooops, Error en la lectura. Intentando de nuevo!')
    return  result      # devuelvo la lectura
    

if __name__ == '__main__':
  # Sensor: Photoresistor
  ldr = LightSensor(6)    # Photoresistor in pin 6
  print('Sensor: Photoresistor GL5516')
  print('   Intensidad luminica = {0:0.2f} %'.format(ldr.value))
  
  print('   Intensidad luminica = {0:0.2f} %'.format(luminosidad(6)))

  
