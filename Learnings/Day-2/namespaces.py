a = "Global" 

def outer():
    a = "Enclosing"

    def inner():
        a = "Local"
        print("a-inner",a)
        
    inner()
    print("a-outer",a)

outer()
print("a-global",a)