def func(list1):
    res = []
    for index,value in enumerate(list1):
        res.append((index,value))
    return res
list1 = [2,3,4,5,6]
result = func(list1)
print(result)