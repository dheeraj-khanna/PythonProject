import testCircle as tc

# This is a sample Python script.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    circle1 = tc.Circle1(42)
    print("Area of circle1 = ", circle1.area())
    # print("Radius of circle1 = ", circle1.__radius)

    circle1.setRadius(66)
    print("Area of circle1 = ", circle1.area())

    # circle1.setRadius(-4)

    circle2 = tc.Circle2(42)
    # print("Area of circle2 = ", circle2.area)
    # # print("Radius of circle2 = ", circle2.radius)

    circle2.radius = 12
    print("Area of circle2 = ", circle2.area)
