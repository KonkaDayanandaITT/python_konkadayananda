import string 
#implicit Type conversion

a = 10
b = 2.6
c = a+b
print(c)
print(type(c))


#Explicit typeconversion

print(int(9.3))
print(int("53"))
print(int(True))
#print(int("8.3"))

print(float(5))
print(float("5.8"))
print(float(True))

print(str(100))
print(str(5.8))
print(str(True))

#converting tuple,set into list
list1 =list ((1,2,3))
print(list1)

list2 = list({1,2,3,5,4})
print(list2) #Here the output will be sorted [1,2,3,4,5]

tuple1 = tuple([1,2,4,6,3,2])
print(tuple1)

set1 = set((1,2,6,5,4,3))
print(set1)

dict1 = dict([(1,'a'),(2,'b')])
print(dict1)
print(type(dict))