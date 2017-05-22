#!/usr/bin/python
import json


#Parameters - Body (data)
"""
params = {"protocol":"v2",
              "device":"RPI1@jmg4carriots.jmg4carriots",
              "at":timestamp,
              "data": dict(
                  temp=27,
                  humd=71)}  
"""                  
hr = 60
temp = 24
l = 0.34
f = carriots.postDataCarriots(hr,temp,l)

#Print in a pretty way
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
    
