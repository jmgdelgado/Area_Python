"""
INSTALACION DEL DRIVER del sensor BMP180
------------------------------------------------------------
INSTALAMOS GIT (si no lo está)
sudo apt-get install git build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_BMP.git
cd Adafruit_Python_BMP
sudo python3 setup.py install

Se conecta mediante protocolo I2C. Hay que habilitarlo en la configuracion de la RPI
Para detectar dispositivos I2C ejecutar el comando
sudo i2cdetect -y 1

el pin del sensor SLC se conecta al pin SLC1 (BCM 3) de la raspberry
el pin del sensor SDA se conecta al pin SDA1 (BCM 2) de la raspberry
el pin VCC del sensor se conecta a 3.3V
el pin GND del sensor se conecta a tierra
"""



import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

print ('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
print ('Presion = {0:0.2f} Pa'.format(sensor.read_pressure()))
print ('Altitud = {0:0.2f} *C'.format(sensor.read_altitude()))
print ('Sealevel Pressure = {0:0.2f} *C'.format(sensor.read_sealevel_pressure()))
