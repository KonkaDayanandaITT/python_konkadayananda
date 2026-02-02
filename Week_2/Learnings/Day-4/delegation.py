class Printer:
    def print_document(self,doc):
        print(f"printing {doc}")
        
class Computer:
    def __init__(self):
        self.printer = Printer()
        
    def print(self, doc):
        self.printer.print_document(doc)
        
computer = Computer()
computer.print("resume.pdf")