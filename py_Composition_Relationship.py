class Motor:
    def __init__(self, model):
        self.model = model

    def start(self):
        print("Motor started.")

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.motor = Motor(model)

    def start(self):
        self.motor.start()
        print(f"Move with {self.brand} {self.motor.model}.")

bmw_motor = Motor("BMW")
bmw_car = Car("BMW", "525")
bmw_motor.start()
bmw_car.start()
