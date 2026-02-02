class Employee:
    name = ""
    id = 0

employee1 = Employee()
employee2 = Employee()

employee1.name = "Ram"
employee1.id   = 101

employee2.name = "Vishnu"
employee2.id   = 102

print(f"Name : {employee1.name}, Id : {employee1.id}")
print(f"Name : {employee2.name}, Id : {employee2.id}")
