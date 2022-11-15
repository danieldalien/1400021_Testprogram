import json
import random
print('Processing done, replying')
data = {}

#data['RandomFloat'] = 10.55555
#data['RandomINT'] = 10
#data['RandomString'] = 'test25'
#data['RandomBool'] = False
#
data['RandomFloat'] = random.uniform(0 , 100)
data['RandomINT'] = random.randrange(100)
#data['RandomString'] = getRandomString(1+random.range(10))
data['RandomString'] = 'test25'
data['RandomBool'] = bool(random.getrandbits(1))

json_data = json.dumps(data)
print(json_data)
print(data)