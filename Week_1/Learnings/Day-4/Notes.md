# Type conversions
## Type conversion means changing a value from one datatype to another
### implicit typeconversion
```
a = 10
b = 1.5
c = a + b
print(c)
print(type(c))
```
### Explicit typeconversion
```
print(int(9.3))
print(int("53"))
print(int(True))
print(int("8.3"))
```
```
list1 =list ((1,2,3))
print(list1)

list2 = list({1,2,3,5,4})
print(list2)
```
# Functions 
## A Function in python is a reusable block of code, you define it once and reuses it again
```
def greet():
    print("Hello guys")
greet()
```
### Function with parameters
```
def sayHello(name):
    print(f"Hello {name}")

sayHello("Ram")
```

### Function with key,value pair
```
def key_value(key,value):
    print(f"My name is {key} and my age is {value}")
key_value("Ram",21)
```

### Keyword only args
```
def keyword_only(*,key):
    print("Throw",key)

keyword_only(key="pen")
```

### Positional only

```
def day(name, /):
    print("Today is",name)

day("Friday")
day("Sunday")
day("Saturday")
```

### combining keyword and positional args

```
def numbers(a,b, /,*,c,d):
    print(f"a={a},b={b},c={c},d={d}")

numbers(10,20,c="30",d ="40")
```
### Lambda Function

```
x = lambda a: a + 10
print(x(5))

y = lambda a , b: a * b
print(y(5,6))
```
### Recursion Function
```
def countdown(n):
    if n < 0:
        print("Countdown is finished")

    else :
        print(n)
        countdown(n-1)

countdown(5)
```

### File Handling
```
"""f = open("demo1.txt","rt")
print(f.read())"""

with open("demo1.txt") as f:
    """print(f.readline())
    print(f.readline())"""
    for ln in f:
        print(ln)
```