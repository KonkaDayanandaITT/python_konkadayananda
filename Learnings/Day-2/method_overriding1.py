class Car:
    name=""
    def run(self):
        print("I can run with petrol/diesel")

class Eeco(Car):
    def run (self):
        super().run()
        print("I can run with CNG")

eeco1 = Eeco()

eeco1.run()