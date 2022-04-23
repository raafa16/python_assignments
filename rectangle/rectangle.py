class Shape:
    def __init__(self):
        pass


class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    # getter for width using property decorator
    @property
    def width(self):
        return self.__width

    # getter for height using property decorator
    @property
    def height(self):
        return self.__height

    # setter function for width
    @width.setter
    def width(self, width):
        self.__width = width

    # setter function for height
    @height.setter
    def height(self, height):
        self.__height = height

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return (self.height * 2) + (self.width * 2)

    def getStats(self):
        print("width:       {}".format(self.width))
        print("height:      {}".format(self.height))
        print("area:        {}".format(self.area))
        print("perimeter:   {}".format(self.perimeter))


def main():
    print("Rectangle a:")
    a = Rectangle(5, 7)
    print("area:        {}".format(a.area))
    print("perimeter:   {}".format(a.perimeter))

    print("")
    print("Rectangle b:")
    b = Rectangle()
    b.width = 10
    b.height = 20
    print(b.getStats())


if __name__ == "__main__":
    main()
