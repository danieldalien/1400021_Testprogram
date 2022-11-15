    
    
import socket
import time
import json
import random
import string
    
data = {}
data['DC-25'] = 0.07
data['DC-30'] = 0.06
data['DC-35'] = 0.075
data['DC-40'] = 0.07

json_data = json.dumps(data)
print(json_data)

def test() :
    for y in range(1,5):
        yield 123


t = test() 

print(t)