numbers = [1,2,3,4,5]
numbers.append(6) # adding element at end
print(numbers)
print(type(numbers))

#lists are mutable 

nums = [1,2,3]
nums[0] = 4
print(nums)

for num in numbers:
    print(num)

for index, value in enumerate(numbers):
    print(index,value)

#list can hold mixed datatypes

data = [1,"run",3.5,True]
print(data)

#common list operations

a = [1,2,3,4,5]
a.append(6)
print(a)
a.insert(1,8)
print(a)
a.remove(5)
print(a)
a.pop()
print(a)

a.append(2)
print(a)
