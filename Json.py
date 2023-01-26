import json

x = '{"name": "dang", "age": 22, "addr": "ha noi"}'

#y = json.dumps(x)
y = json.loads(x)
print(y["age"])