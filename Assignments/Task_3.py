print("----Sorting a list----")
arr = [6,4,8,3,9,10]
n = len(arr)

for i in range(n):
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
print(arr)

#Dict
print("----Sorting Dictionary----")
marks = {
    "Vishnu" : 90,
    "Ram" : 95,
    "Laxman" : 80,
    "Varun" :96
}

list1 = []

for key in marks:
    list1.append((key,marks[key]))

l = len(list1)

for i in range(l):
    for j in range(l-1):
        if list1[j][1] > list1[j+1][1]:
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp

sorted_marks={}
for key,value in list1:
    sorted_marks[key] = value

print(sorted_marks)
