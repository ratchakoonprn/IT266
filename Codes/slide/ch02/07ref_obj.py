class Box():
    """
    An instance is a box originated from (0,0).
    to create a box type:
    b = Box(1,2)
    """
    def __init__(self, x, y):
        """
        Creates a box with (x,y)
        """
        self.x = x
        self.y = y

    def area(self):
        """
        Prints the area of the box
        """
        print(self.x*self.y)

# เข้าถึงตัวแปรของ object
b = Box(3,5)
print(b.x)
print(b.y)
print(b.area())