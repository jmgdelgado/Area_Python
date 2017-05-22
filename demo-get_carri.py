#!/usr/bin/python
import json
from mysensores import carriots


#Request
f = carriots.getDataCarriots(1)

#Print response
#print(f.read().decode('utf-8'))

#Print in a pretty way
data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
                
