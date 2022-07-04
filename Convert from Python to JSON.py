#Convert from Python to JSON & JESON to Python

import json

x = '{ "name":"John", "age":30, "city":"New York"}'
y=json.loads(x)
print(y["age"])

a={"name":"sourav", "age":28, "city":"dhaka"}
b=json.dumps(a)

print(b)
