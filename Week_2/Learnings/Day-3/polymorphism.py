class Developers:
    def __init__(self, name, experience):
        self.name= name
        self.experience = experience

    def info(self):
        print(f"My name is {self.name}, I'm working since {self.experience} years")

    def work(self):
        print("Building Websites")

class Qa_Testing:
    def __init__(self , name, experience):
        self.name = name
        self.experience = experience

    def info(self):
        print(f"My name is {self.name}, I'm working since {self.experience} years")

    def work(self):
        print("Testing functionalities")

developer1 = Developers("Ram",5)
qatester1 = Qa_Testing("Vishnu",3)
for employee in (developer1,qatester1):
    employee.info()
    employee.work()