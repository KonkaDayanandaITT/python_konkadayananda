class SafeFilewrite:
    def __init__(self, filename):
        self.filename = filename
        
    def __enter__(self):
        self.backup = open(self.filename).read()
        self.file = open(self.filename, "w")
        return self.file
    
    def __exit__(self, exc_type, exc_value, exc_tp):
        self.file.close()
        
        if exc_type:
            print("Write failed -> restoring the file")
            with open(self.filename, "w") as f:
                f.write(self.backup)
                
        return false