class Car:
    def __init__(self, name: str, model: float):
        self.name = name
        self.model = model

    def get_name(self):
        return self.name

car = Car("BMW", 362623.2)

print(car.get_name())