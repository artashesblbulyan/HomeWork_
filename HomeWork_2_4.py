import math


class Triangle:
    triangle_amount = 0

    def __new__(cls, *args, **kwargs):
        cls.triangle_amount += 1
        return super().__new__(cls)

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def __repr__(self):
        return f"{self.triangles_equal()}"

    def __eq__(self, other):
        return self.triangles_equal() == other.triangles_equal()

    def __lt__(self, other):
        if self.triangles_equal()[0] < other.triangles_equal()[0] and \
                self.triangles_equal()[1] < other.triangles_equal()[1] and \
                self.triangles_equal()[2] < other.triangles_equal()[2]:
            return self.triangles_equal() < other.triangles_equal()
        else:
            return False

    def __gt__(self, other):
        if self.triangles_equal()[0] > other.triangles_equal()[0] and \
                self.triangles_equal()[1] > other.triangles_equal()[1] and \
                self.triangles_equal()[2] > other.triangles_equal()[2]:
            return self.triangles_equal() > other.triangles_equal()
        else:
            return False

    def triangles_equal(self):
        return sorted([self.side_1, self.side_2, self.side_3])

    def validate_triangle(self):
        """
        checks whether a triangle can be constructed
        with the given numbers, if yes then
        it is a right triangle or not
        """
        validate_tri = self.triangles_equal()
        if ((validate_tri[2] + validate_tri[1]) > validate_tri[0]) \
                and ((validate_tri[0] + validate_tri[1]) > validate_tri[2]) \
                and ((validate_tri[2] + validate_tri[0]) > validate_tri[1]):
            if validate_tri[2]**2 == (validate_tri[0]**2 + validate_tri[1]**2):
                return "it's a right triangle"
            else:
                return True
        else:
            print("There can be no triangle with sides of this size")
            return False

    def triangles_area(self):
        """
        calculates the area of a triangle on the
        perimeter where P is equal to half the perimeter
        """
        if self.validate_triangle():
            p = self.triangles_perimeter()/2
            s = math.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3))
            return s

    def triangles_perimeter(self):
        if self.validate_triangle():
            return self.side_1 + self.side_2 + self.side_3


a = Triangle(5, 3, 4)
b = Triangle(8, 6, 9)
c = Triangle(8, 6, 9)
d = Triangle(8, 6, 9)
e = Triangle(8, 6, 9)
g = Triangle(8, 6, 9)
print(Triangle.triangle_amount, "the number of created objects")
print(a.triangles_perimeter(), "perimeter")
print(a.triangles_area(), "area")
print(a.validate_triangle(), )
print(a.triangles_equal())
print(Triangle(9, 2, 3) == Triangle(2, 3, 9))
print(Triangle(3, 4, 5) < Triangle(6, 5, 4))
print(Triangle(9, 9, 7) > Triangle(8, 6, 5))
print(Triangle(4, 5, 3) > Triangle(8, 6, 10))
print(Triangle(4, 4, 7) < Triangle(8, 6, 10))




