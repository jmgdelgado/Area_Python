#! usr/bin/python3
# ---  #importo las librerias que necesito
import http.client
import urllib.request
import urllib.parse
import json
import time, datetime

# ---  DEFINO VARIABLES ---
get_api_url = "http://api.carriots.com/streams/?device=***MIId. Developer:***
api_key = "***MIAPIKEY***"
post_api_url= "http://api.carriots.com/streams"
device = "***MIDISPOSITIVO***"

def getDataCarriots(max):     # Creo una funcion para hacer GET del DISPOSITIVO
    #Parametros
    get_timestamp = int(time.time())
    get_params = {'order':-1}   #orden inverso, primero los nuevos 
    get_bData = json.dumps(get_params).encode('ascii')
    #Cabeceras
    get_header = {"User-Agent": "***MIId. Developer:***",
          "Content-Type": "application/json",
          "carriots.apikey": api_key}

    #LLamada
    req = urllib.request.Request(get_api_url,get_bData,get_header)
    # req.get_method = lambda: "GET" ' es  necesario para cambiar el comportamiento por defecto de Request de POST a GET. 
    req.get_method = lambda:"GET"
    f = urllib.request.urlopen(req)

    return  f  

def postDataCarriots(hr,temp, light):      # Creo una funcion para hacer POST al DISPOSITIVO

    #Obtenemos la hora del sistema
    timestamp = int(time.time())

    #Parametros
    post_params = {"protocol" : "v2",
          "device": device,
          "at" : int(time.mktime(datetime.datetime.utcnow().timetuple())),
          "data" : {"temp":temp,"hum":hr, "light":light}}
    post_bData = json.dumps(post_params).encode('ascii')

    #Cabeceras 
    post_header = {
          "Accept": "application/json",
          "User-Agent": "***MIId. Developer:***",
          "Content-Type": "application/vnd.carriots.api.v2+json",
          "carriots.apikey": api_key}
    #LLamada
    req = urllib.request.Request(post_api_url,post_bData,post_header)
    f = urllib.request.urlopen(req)
   
    return f
