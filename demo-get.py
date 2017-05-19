#!/usr/bin/python
import http.client
import urllib.request
import urllib.parse
import json
import time

api_url = "https://api.carriots.com/devices"    # Lista de dispositivos
#api_url = "https://api.carriots.com/streams/"  # Datos de dispositivos
api_key = "eca83189ebe6f566b328949ad9fd47d857f31c82c197a190f9c9fd38464c9c66"

#Parameters - Body
timestamp = int(time.time())
params = {"order":-1}  # Reverse order, to get newest first
binary_data = json.dumps(params).encode('ascii')

#Header
header = {"User-Agent": "raspberrycarriots",
              "Content-Type": "application/json",
              "carriots.apikey": api_key}

#Request
req = urllib.request.Request(api_url,binary_data,header)
req.get_method = lambda:"GET"
f = urllib.request.urlopen(req)

#Print response
#print(f.read().decode('utf-8'))

#Print in a pretty way
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
                
