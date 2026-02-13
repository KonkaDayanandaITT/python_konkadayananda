from enum import Enum


class Mode(Enum):
    OFF = "off"
    HEATING = "heating"
    COOLING = "cooling"


class Thermostat:
    def __init__(self, current):
        self.current = current
        self.target = current
        self.mode = Mode.OFF

    def update_mode(self):
        if self.current < self.target:
            self.mode = Mode.HEATING
        elif self.current > self.target:
            self.mode = Mode.COOLING
        else:
            self.mode = Mode.OFF

    def set_target(self, target):
        if target < 0:
            raise ValueError("Temperature cannot be negative")
        self.target = target
        self.update_mode()

    def status(self):
        return f"Current: {self.current}, Target:{self.target}, Mode:{self.mode.value}"


try:
    current = int(input("Enter current temperature: "))
    target = int(input("Enter target temperature: "))
    
    if current < 0 :
        raise ValueError("Temperature cannot be negative")

    thermostat = Thermostat(current)
    thermostat.set_target(target)
    print(thermostat.status())
except ValueError as e:
    print("Error: ", e)
