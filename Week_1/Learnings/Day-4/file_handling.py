"""f = open("demo1.txt","rt")
print(f.read())"""

with open("demo1.txt") as f:
    """print(f.readline())
    print(f.readline())"""
    for ln in f:
        print(ln)

with open("demo1.txt",'w') as f:
    f.write("Hi guys")




