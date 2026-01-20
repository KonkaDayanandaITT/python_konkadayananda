class Animal:
    name = ""
    def eat(self):
        print("i can eat")

class Dog(Animal):
    def display(self):
        print(f"My name is {self.name}")

chichuva = Dog()
chichuva.name = "Bliss"
chichuva.eat()

chichuva.display()
