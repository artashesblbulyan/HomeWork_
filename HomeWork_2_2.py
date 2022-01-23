import datetime


class Circle:

    def __init__(self, radius):
        if not(isinstance(radius, (int, float))):
            raise TypeError(f"{radius} is not an instance of int or float")
        self.radius = radius

    def area_circle(self):
        area_ = 3.14 * (self.radius ** 2)
        return area_

    def perimeter_circle(self):
        perimeter_ = 3.14 * self.radius * 2
        return perimeter_


a = Circle(25)
print(a.area_circle())
print(a.perimeter_circle())


class Human:

    def __init__(self, name, surname, age, height, weight):
        if not(isinstance(age, int) and isinstance(height, (int, float)) and isinstance(weight, (int, float))):
            raise TypeError(f"{age},{height},{weight} is not an instance of int or float")
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height
        self.weight = weight

    def years_100(self):
        now = datetime.datetime.now()
        age_100 = now.year+100 - self.age
        return age_100

    def optimal_weight(self):
        # de = self.weight/(self.height ** 2)
        opt_weight = (self.height-100) - (self.height-150)/2
        return opt_weight

    def present(self):
        print(f"Hello {self.name} {self.surname} your weight is {self.weight} kg \n your optimal weight should be"
              f" {self.optimal_weight()} kg \n you will turn 100 in {self.years_100()} ")


b = Human("Artashes", "Blbulyan", 29, 175, 70)

# print(b.years_100())
# print(b.optimal_weight())
b.present()
