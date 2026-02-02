class Aquatic_animal():
     name =""
     def swim(self):
        print("I live on water")

class Land_animal():
    def run(self):
        print("I live on land")

class Frog(Aquatic_animal,Land_animal):
    pass

frog1 = Frog()
frog1.swim()
frog1.run()