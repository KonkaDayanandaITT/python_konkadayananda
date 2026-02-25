import json

x = '{"name" : "ram", "age": 30, "city": "swiss"}'
y = json.loads(x)

print(y["age"])  #converts from json to python 
#for json->python we will use json.loads()

#converting python to json
p = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

z = json.dumps(p)
print(z)


print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))