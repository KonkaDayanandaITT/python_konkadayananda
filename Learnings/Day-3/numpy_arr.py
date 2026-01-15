import numpy as np

arr = np.array([1,2,3,4])
list1=list(arr)
list1.append(5)
arr=np.array(list1)
# arr.append(5)
print(arr)
print(arr*2)

#types 

a = np.array([1,2,3,4,5])

b = np.array([[1,2,3],[4,5,6]])

c = np.array([[[1,2],[3,4],[4,5]]])

print(a)
print(b)
print(c)