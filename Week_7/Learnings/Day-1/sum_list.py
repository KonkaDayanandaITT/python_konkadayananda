# lst = [98,4,95,6,43,43,147,82,54]
# even = []
# for num in lst:
#     if num % 2 == 0:
#         even.append(num)
        
# print(even)

# max = lst[0]

# for num in lst:
#     if num > max:
#         max, num = num, max
# print(max)

# str_1 = "blooper"
# rev_str = ""

# for alpha in str_1:
#     rev_str = alpha + rev_str 
    
# print(rev_str)

# strng = "banana"
# occ_a =0

# for i in strng:
#     if i == "a":
#         occ_a += 1
        
# print(occ_a)



# occurances = {}

# for num in nums:
#     if num not in occurances:
#         occurances[num] = 1
#     else:
#         occurances[num] += 1
# print(occurances)
nums = [1,2,2,3,4,1,2,5,3]

target = {
    "even":{
        "numbers":[],
        "count":0
        },
    "odd":{
        "numbers":[],
        "count":0
    }
}

for num in nums:
    if num % 2 == 0:
        if num not in target["even"]["numbers"]:
            target["even"]["numbers"].append(num)
            target["even"]["count"] += 1
    else:
        if num not in target["odd"]["numbers"]:
            target["odd"]["numbers"].append(num)
            target["odd"]["count"] += 1
print(target)