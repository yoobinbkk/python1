# Ex03_json.py

f = open('./data/temp.json', 'r', encoding='utf-8')
data = f.read()
f.close()

print(data)
print(type(data))


import json
x = json.loads(data)

print(x)
print(type(x))

for k, val in x.items():
    print(k, '\t', val)
    print(k, '\t', val['Job'])