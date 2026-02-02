from enum import Enum

class Mode(Enum):
    OFF = "off"
    HEATING = "heating"
    COOLING = "cooling"
    
class Thermostat:
    def __init__(self, current, target):
        if current < 0 or target < 0:
            print("Temparature Cannot be negative")
            return
        
        self.current = current
        self.target = target
        self.mode = Mode.OFF
        self.update_mode()
        
    def update_mode(self):
        if self.current < self.target:
            self.mode = Mode.HEATING
        elif self.current > self.target:
            self.mode = Mode.COOLING
        else:
            self.Mode = Mode.OFF
            
    def update_current(self, new_current):
        if new_current < 0:
            print("Temparature cannot be negative")
            return
        
        self.current = new_current
        self.update_mode()
        
    def status(self):
        return f"Current: {self.current}, Target:{self.target}, Mode:{self.mode.value}"
    

try:
    current = int(input("Enter current temperature: "))
    target = int(input("Enter target temparature: "))
    
    thermostat = Thermostat(current, target)
    print(thermostat.status())
    
    new_curr = int(input("Update current temparature: "))
    thermostat.update_current(new_curr)
    print(thermostat.status()) 
except ValueError as e:
    print("Error: ", e) 