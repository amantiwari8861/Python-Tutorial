class Component:
    def __init__(self, name=None):
        self.name = name

    def display_info(self):
        print("Component:", self.name)


class Vehicle(Component):
    def __init__(self, name=None, wheels=None, engine=None):
        super().__init__(name)
        self.wheels = wheels
        self.engine = engine

    def display_info(self):
        super().display_info()
        print("Wheels:", self.wheels)
        self.engine.display_info()


class Engine(Component):
    def __init__(self, name=None, horsepower=None):
        super().__init__(name)
        self.horsepower = horsepower

    def display_info(self):
        super().display_info()
        print("Horsepower:", self.horsepower)


class Car:
    def __init__(self, name=None, wheels=None, horsepower=None, model=None):
        self.vehicle = Vehicle(name, wheels, Engine("Engine", horsepower))
        self.model = model

    def display_info(self):
        self.vehicle.display_info()
        print("Model:", self.model)


# Example usage
my_car = Car("Car", 4, 200, "Toyota")
my_car.display_info()

#   def __init__(self, name=None, wheels=None, horsepower=None, model=None):
#         Vehicle.__init__(self, name, wheels)
#         Engine.__init__(self, name, horsepower)  # Pass 'name' to Engine constructor
#         self.model = model