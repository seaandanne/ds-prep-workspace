
class Triangle:

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return (self.base * self.height) / 2


def is_equilateral(var1,var2,var3):
    if var1==var2==var3:
        return True
    else:
        return False
    
description = "this is a module named triangle"


if __name__ == "__main__":
    triangle = Triangle(base,height)
    print("Area is {}".format(triangle.get_area(),))


