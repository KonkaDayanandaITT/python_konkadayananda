# a dict stores data as key value pairs and it is mutable

student = {
    "name" : "ram",
    "age" : 21,
    "cource" : "python",
    "city" : "hyd"
} 
print(student)
print(student["cource"])
print(student["age"])
print(student.get("age"))
print(student.get("name"))

student["city"] = "blr"
print(student["city"])

for key in student:
    print(key)

for value in student.values():
    print(value)
for key, value in student.items():
    print(key,value)