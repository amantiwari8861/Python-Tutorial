# Making Getters and Setter methods
# class Celsius:
#     def __init__(self, temperature=0):
#         self.set_temperature(temperature)
#     def to_fahrenheit(self):
#         return (self.get_temperature() * 1.8) + 32
#     # getter method
#     def get_temperature(self):
#         return self._temperature
#     # setter method
#     def set_temperature(self, value):
#         if value < -273.15:
#             raise ValueError("Temperature below -273.15 is not possible.")
#         self._temperature = value


# Create a new object, set_temperature() internally called by __init__
# human = Celsius(37)

# # Get the temperature attribute via a getter
# print(human.get_temperature())

# # Get the to_fahrenheit method, get_temperature() called by the method itself
# print(human.to_fahrenheit())

# # new constraint implementation
# human.set_temperature(-300)

# Get the to_fahreheit method
# print(human.to_fahrenheit())


# However, the bigger problem with the above update is that all the programs that implemented our previous class have to modify their code from obj.temperature to obj.get_temperature() and all expressions like obj.temperature = val to obj.set_temperature(val).
# This refactoring can cause problems while dealing with hundreds of thousands of lines of codes.
# All in all, our new update was not backwards compatible. This is where @property comes to rescue.
# The property Class
# A pythonic way to deal with the above problem is to use the property class. Here is how we can update our code:

# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)

human = Celsius(37)
print(human.temperature)
print(human.to_fahrenheit())
human.temperature = -300