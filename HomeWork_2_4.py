import math


class Triangle:
    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def __repr__(self):
        return f"{self.triangles_equal()}"

    def __eq__(self, other):
        return self.triangles_equal() == other.triangles_equal()

    def __lt__(self, other):
        return self.triangles_equal() < other.triangles_equal()

    def __gt__(self, other):
        return self.triangles_equal() > other.triangles_equal()

    def triangles_equal(self):
        triangles_equal_list = (self.side_1, self.side_2, self.side_3)
        triangles_equal_list = sorted(triangles_equal_list)
        return triangles_equal_list

    def rectangular(self):
        """
        checks whether a triangle can be constructed
        with the given numbers, if yes then
        it is a right triangle or not
        """
        rectangular = self.triangles_equal()
        if ((rectangular[2] + rectangular[1]) > rectangular[0]) \
                and ((rectangular[0] + rectangular[1]) > rectangular[2]) \
                and ((rectangular[2] + rectangular[0]) > rectangular[1]):
            if rectangular[2]**2 == (rectangular[0]**2 + rectangular[1]**2):
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
        if self.rectangular():
            p = self.triangles_perimeter()/2
            s = math.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3))
            return s

    def triangles_perimeter(self):
        if self.rectangular():
            return self.side_1 + self.side_2 + self.side_3


a = Triangle(3, 4, 5)
b = Triangle(8, 6, 9)
print(a.triangles_perimeter())
print(b.triangles_perimeter())
print(a.triangles_area())
print(b.triangles_area())
print(a.rectangular())
print(b.rectangular())
print(a.triangles_equal())
print(b.triangles_equal())
print(Triangle(9, 2, 3) > Triangle(5, 3, 9))
print(Triangle(9, 2, 3) < Triangle(5, 3, 9))
print(Triangle(9, 2, 3) == Triangle(2, 3, 9))
# print([1,2,3] == [1,2,3])

