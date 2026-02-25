import mymodule
import platform

x = platform.system()
print(x)
print(mymodule.person1["name"])
print(mymodule.person1["country"])
mymodule.person1["country"] = "swiss"
print(mymodule.person1["country"])