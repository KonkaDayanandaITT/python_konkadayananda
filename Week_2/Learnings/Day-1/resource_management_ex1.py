# file = open("sample.txt", "r")
# data = file.read()
# # forgot to close the file

# # The above code is bad resource management

# with open("sample.txt", "r") as f:
#     data = f.read()             #This is good resource management


try:
    with open("sample.txt", "r") as f:
        data = f.read()
        print(data)

except FileNotFoundError:
    print("File not Found")
