class Room:
    length = 0.0
    breadth = 0.0
    def measure(self):
        print("Area of romm =",self.length * self.breadth)

studyroom1 = Room()
studyroom1.length = 30.5
studyroom1.breadth = 25.5
studyroom1.measure()