def numbers():
    print("start")
    yield 1
    print("middle")
    yield 2
    print("end")
    
gen = numbers()
next(gen)
next(gen)
next(gen)