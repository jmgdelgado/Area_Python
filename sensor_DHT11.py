"""
INSTALACION DEL DRIVER (Yo lo he usado con un dht11 con placa, no necesita pull up)
------------------------------------------------------------
INSTALAMOS GIT (si no lo está)
sudo apt-get install git build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python3 setup.py install
"""

#!/usr/bin/python
import sys
import Adafruit_DHT

tipo_sensor = 11  # Numero del Sensor DHT_11
pin_datos = 4     # Pin donde se conecta a la rasberry para recibir los datos, en este caso GPIO4
# El pin DATA del sensor se conecta al pin GPIO de la rasberry
# El pin VCC del sensor se conecta al 3.3V de la rasberry. Tambien se puede conectar al de 5V.
# El pin GND del sensor se conecta a tierra

while True:
    humidity, temperature = Adafruit_DHT.read_retry(tipo_sensor,pin_datos)

    print ('Temp: {0:0.1f} C Humidity: {1:0.1f} %'.format(temperature,humidity))
    
