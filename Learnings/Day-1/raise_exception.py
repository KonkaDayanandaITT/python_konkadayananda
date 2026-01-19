age = int(input("Enter a number:"))

if(age < 18):
    raise ValueError("Age must be 18 or above")