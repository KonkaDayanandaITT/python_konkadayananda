class MyResource:
    def __enter__(self):
        print("Resource Acquired")
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Releasing resource")
        
    def printing(self):
        print("Hello")


with MyResource() as r:
    print("Using Resource")
    #print(r.__enter__())
    r.printing()