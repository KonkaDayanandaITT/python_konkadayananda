class FileWrapper:
    def __init__(self, file):
        self.file = file
        
    def write(self, text):
        print("writing to file")
        self.file.write(text)
        
    def close(self):
        print("closing file")
        self.file.close()
        

f= open("test.txt", "w")
fw = FileWrapper(f)

fw.write("Hello")
fw.close()