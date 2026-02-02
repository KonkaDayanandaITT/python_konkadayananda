class Student:
    def __init__ (self, name ="Ramarao",age = 34):
        self.name = name
        self.age = age

s1 = Student()
s2 = Student("Bharat",29)

print("Name: {}, Age : {}".format(s1.name,s1.age))
print("Name : {}, Age :{}".format(s2.name,s2.age))