class Engine:
    def start(self):
        print("Engine started")


class Bike:
    def __init__(self, name):
        self.name = name
        self.engine = Engine()

    def start(self):
        self.engine.start()
        print(f"{self.name} bike started")


bike1 = Bike("Honda")
bike1.start()