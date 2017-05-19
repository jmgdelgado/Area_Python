import sys
sys.path.append('/home/pi/')
import Adafruit_BMP.BMP085 as BMP085

sensor = BMP085.BMP085()

print ('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
print ('Presion = {0:0.2f} Pa'.format(sensor.read_pressure()))
print ('Altitud = {0:0.2f} *C'.format(sensor.read_altitude()))
print ('Sealevel Pressure = {0:0.2f} *C'.format(sensor.read_sealevel_pressure()))
