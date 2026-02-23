# with open("marks.txt", "w") as f:
#     f.write("Math : 90\n")
#     f.write("English : 85\n")
    
# with open("data.txt", "r") as f:
#     text = f.read()
#     res = text.title()
# with open("clean.txt", "w") as f:
#     f.write(res)

with open("clean.txt", "r") as f:
    content = f.read()
    res = content.split()
    
count = 0

for index in res:
    count += 1
    
print(count)