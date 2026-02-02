from engine import Engine

class Bike:
    def __init__(self, name):
        self.name = name
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print(f"{self.name} bike started")
    
    def park(self):
        self.stop()
        print(f"{self.name} is parked")    
        
    def stop(self):
        self.engine.stop()
        print(f"{self.name} stopped")

bike1 = Bike("Honda")
bike1.start()
bike1.park()