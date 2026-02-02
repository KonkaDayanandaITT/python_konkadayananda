def greet():
    print("hello")
    
say = greet #function stored in variable
say()


def outer():
    x = 10
    def inner():
        print(x) #uses x from outer
    return inner
fn = outer()
fn()


