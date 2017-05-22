#! usr/bin/python3
# ---  #importo las librerias que necesito
import http.client
import urllib.request
import urllib.parse
import json
import time, datetime

# ---  DEFINO VARIABLES ---
device = "RPI1@jmg4carriots.jmg4carriots" # Replace with the "id_developer" of your devic
## get_api_url = "http://api.carriots.com/streams/?device=***MIId. Developer:***
get_api_url = "https://api.carriots.com/devices/" + device + "/streams/"  ##?order=-1
api_key = "eca83189ebe6f566b328949ad9fd47d857f31c82c197a190f9c9fd38464c9c66"
post_api_url= "http://api.carriots.com/streams"



def getDataCarriots(max):     # Creo una funcion para hacer GET del DISPOSITIVO
    #Parametros
    get_timestamp = int(time.time())
    get_params = {'order':-1}   #orden inverso, primero los nuevos 
    get_bData = json.dumps(get_params).encode('ascii')
    #Cabeceras
    get_header = {"User-Agent": "raspberrycarriots",
          "Content-Type": "application/json",
          "carriots.apikey": api_key}

    #LLamada
    req = urllib.request.Request(get_api_url,get_bData,get_header)
    # req.get_method = lambda: "GET" ' es  necesario para cambiar el comportamiento por defecto de Request de POST a GET. 
    req.get_method = lambda:"GET"
    f = urllib.request.urlopen(req)

    return  f  

## def postDataCarriots(hr,temp, light):      # Creo una funcion para hacer POST al DISPOSITIVO
def postDataCarriots(datos):      # Creo una funcion para hacer POST al DISPOSITIVO    

    #Obtenemos la hora del sistema
    timestamp = int(time.time())

    #Parametros
    post_params = {"protocol" : "v2",
          "device": device,
          "at" : int(time.mktime(datetime.datetime.utcnow().timetuple())),
          "data" : datos}         
          ##"data" : {"temp":temp,"hum":hr, "light":light}}
    post_bData = json.dumps(post_params).encode('ascii')

    #Cabeceras 
    post_header = {
          "Accept": "application/json",
          "User-Agent": "raspberrycarriots",
          "Content-Type": "application/vnd.carriots.api.v2+json",
          "carriots.apikey": api_key}
    #LLamada
    req = urllib.request.Request(post_api_url,post_bData,post_header)
    f = urllib.request.urlopen(req)
   
    return f


if __name__ == '__main__':
    getDataCarriots(1)  
