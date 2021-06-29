"""
In this Try It Out, you start by creating a simple Circle1 class that has only one attribute and two
callable methods: setRadius() and area() . You then create a second class, Circle2 , which makes
radius and area properties. Finally, you see how the use of properties simplifies the use of the class in
client code.

"""

class Circle1:

    def __init__(self, radius):
        self.__radius =  radius

    def setRadius(self,newValue):
        if newValue > 0:
            self.__radius = newValue
        else: raise ValueError("Value must be positive")

    def area(self):
        return 3.14159 * (self.__radius ** 2)


class Circle2:

    def __init__(self, radius):
        self.__radius = radius

    def __setRadius(self, newValue):
        if newValue >= 0:
            self.__radius = newValue
        else: raise ValueError("Value must be positive")
    radius = property(None, __setRadius)

    @property
    def area(self):
        return 3.14159 * (self.__radius ** 2)