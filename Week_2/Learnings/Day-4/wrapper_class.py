class ListWrapper:
    def __init__(self,data):
        self._data = data
        
    def add(self, item):
        print("Adding item:", item)
        self._data.append(item)
        
    def get_all(self):
        print("Accessing list")
        return self._data
    
    
lst = ListWrapper([])
lst.add(10)
lst.add(20)

print(lst.get_all())