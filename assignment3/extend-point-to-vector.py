# Task 5: Extending a Class

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
    
class Vector(Point):
    def __str__(self):
        return f"Vector<{self.x}, {self.y}>"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    

if __name__ == "__main__":
    # Demonstrate Point methods
    p1 = Point(1, 2)
    p2 = Point(4, 6)
    p3 = Point(1, 2)

    print("p1:", p1)
    print("p2:", p2)
    print("p1 == p2:", p1 == p2)
    print("p1 == p3:", p1 == p3)
    print("Euclidean distance between p1 and p2:", p1.distance(p2))

    print("-" * 40)

    # Demonstrate Vector methods
    v1 = Vector(2, 3)
    v2 = Vector(5, 7)
    v3 = v1 + v2

    print("v1:", v1)
    print("v2:", v2)
    print("v1 + v2 =", v3)
    print("v1 == Vector(2, 3):", v1 == Vector(2, 3))