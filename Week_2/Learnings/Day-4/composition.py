class Engine:
    def start(self):
        print("Engine is running")
        
class Car:
    def __init__(self):
        self.engine = Engine()
        
    def drive(self):
        self.engine.start()
        print("car is moving")
        
car = Car()
car.drive()