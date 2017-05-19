#!/usr/bin/python
import http.client
import urllib.request
import urllib.parse
import json

api_url = "https://api.carriots.com/streams/0c501aea02469f846cc674472d68ba8c88fde692945f9648752e05919d0cc4cc@jmg4carriots.jmg4carriots/" # Replace with the strem "id_developer"
#device = "RPI1@jmg4carriots.jmg4carriots" # Replace with the "id_developer" of your device
api_key = "eca83189ebe6f566b328949ad9fd47d857f31c82c197a190f9c9fd38464c9c66"


#Parameters - Body (data)
params = {}  
binary_data = json.dumps(params).encode('ascii')

#Header
header = {"User-Agent": "raspberrycarriots",
              "Content-Type": "application/json",
              "carriots.apikey": api_key}

#Request
req = urllib.request.Request(api_url,binary_data,header)
req.get_method = lambda: "DELETE"
f = urllib.request.urlopen(req)


#Print in a pretty way
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
    
