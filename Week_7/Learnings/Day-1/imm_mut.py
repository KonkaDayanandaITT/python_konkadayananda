# a = [1, 2] 
# print(id(a))
# a = a + [3]
# print(id(a))
# print(a) #[1, 2, 3]creates new list

# b = [3,4]
# print(id(b))
# b += [5]
# # b.extend([6])
# b.append(6)
# b.append(7,)
# print(id(b))
# print(b)

# c =[3,4]
# c.extend([3,4])
# #c.append([2,3])
# print(c)

# print(6 and 5)
# print(12 and 0)
# print(89 and 9)
# print(873 and 2003)

# a = [1,2, 3]
# print(3 in a)

# b = {1, 2, 3, 4}
# print(4 in b)

# c = (1, 2, 3)
# print(3 in c )

# print( max = {a : 1, b : 2})
# print(1 in max)

# s = "10010"
# a = int(s, 2)
# print(a)
# b = float(s)
# print(b)
# c = '4'
# print("ASCII of '4' :",ord(c))
# print("56 in hex:", hex(56))
# print("56 in oct:", oct(56))

# s = "cheeks"

# print(tuple(s))
# print(set(s))
# print(list(s))
# print(list(dict.fromkeys(s)))
# print(set(""))


# a = 1
# tup = (('a', 1), ('f', 2), ('g', 3))
# print("To complex:", complex(1, 2))
# print("To string:", str(a))
# print("To dict:", dict(tup))

# def func(n):
#     print("Hello")
    
# print(func(0))
# func(0)

# def evenOdd(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
        
# number = 34
# evenOdd(number)

# def myfunc(x, y=50, *args):
#     print(x)
#     print(y)
#     print(args)
# myfunc(5, 10, 20)

def outer():
    x = [1, 2]
    def inner():
        x.append(3)
        print(x)
    inner()
    print(x)
outer()