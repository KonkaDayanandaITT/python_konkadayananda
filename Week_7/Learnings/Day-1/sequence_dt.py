# s = " hello guys "

# # print(s)

# # for index in s:
# #     print(index) 

# print(s[0]) 


# print(s[-1])

# print(s[::-1])
# print(s.capitalize())
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())

# a = ["Geeks", "For", "Geeks"]
# print("Accessing element from the list")
# print(a[0])
# print(a[2])

# print("Accessing element using negative indexing")
# print(a[-2])
# print(a[-3])

# initiate empty tuple
# tup1 = ('hi',)

# tup2 = ('Geeks', 'For')
# #print("\nTuple with the use of String: ", tup2)
# print(tup1+tup2)

# initializing empty set
# s1 = set()

# s1 = set("GeeksForGeeks")
# print("Set with the use of String: ", s1)

# s2 = set(["Geeks", "For", "Geeks"])
# print("Set with the use of List: ", s2)

# set1 = set(["Geeks", "For", "Geeks"]) #Duplicates are removed automatically
# print(set1) 

# # loop through set
# for i in set1:
#    print(i, end=" ") #prints elements one by one
  
# # check if item exist in set   
# print("Geeks" in set1)


d = {1: 'Geeks', "name": 'For', 3: 'close'}
print(d)

# creating dictionary using dict() constructor
# d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
# print(type(d1))
# print(d1)

print(d['name'])
print(d.get(3))