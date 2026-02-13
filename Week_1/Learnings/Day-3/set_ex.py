#set is used to store unique elements and it is unordered

nums = {1,2,3,3}
print(nums) # it will automatically remove 3
print(type(nums))

nums.add(8) # it will add at first
print(nums)

nums.remove(3) # one 3 is deleted automatically and remaining 3 will also removed now
print(nums)

print(1 in nums)
print(10 in nums)

a = {1,2,3}
b = {3,4,5}
print(a & b) #intersection
print(a | b) # union
print(a - b) # difference
