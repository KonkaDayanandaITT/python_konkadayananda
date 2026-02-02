from array import array

arr = array('i',[1,2,3,4])
arr.append(5)
print(type(arr))
for i in arr:
    print(i)