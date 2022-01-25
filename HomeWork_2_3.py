class Country:
    def __init__(self, name, continent, *args, **kwargs):
        self.name = name
        self.continent = continent
        # print("in is Country", args, kwargs)
        super().__init__(*args, **kwargs)

    def present_country(self):
        return f"Made in {self.name} {self.continent}"


class Brand:
    def __init__(self, brand_name, busnes_start_date, *args, **kwargs):
        self.brand_name = brand_name
        self.busnes_start_date = busnes_start_date
        # print("in is Brand", args, kwargs)
        super().__init__(*args, **kwargs)

    def present_brand(self):
        return f"by{self.brand_name} in the {self.busnes_start_date}"


class Season:
    def __init__(self, season_name, average_temperature, *args, **kwargs):
        self.season_name = season_name
        self.average_temperature = average_temperature
        # print("in is Season", args, kwargs)
        super().__init__(*args, **kwargs)

    def present_season(self):

        return f"of {self.season_name} where the average temperature reaches {self.average_temperature}"


class Product(Country, Brand, Season):
    def __init__(self, product_name, product_type, product_price, product_quantity, *args, **kwargs):
        self.product_name = product_name
        self.product_type = product_type
        self.product_price = product_price
        self.product_quantity = product_quantity
        # print("in is sport", args, kwargs)
        super().__init__(*args, **kwargs)

    def present(self):

        print(f"Product Name {self.product_name} Product Type {self.product_type} \n"
              f" Cigarette Price {self.product_price}"
              f" Quantity {self.product_quantity} pieces\n {super().present_country()} {super().present_brand()} \n "
              f"{super().present_season()}")

    def discount(self, product_price_percent):
        """
        deducts the mentioned percentage from the price of the product
        parameter : product_price_percent
        return :self.product_price
        """
        self.product_price = self.product_price - (self.product_price * (product_price_percent/100))
        return self.product_price

    def increase(self, product_quantity_increase):
        """
        increases the product by the specified quantity
        parameter : product_quantity_increase
        return :self.product_quantity
        """
        self.product_quantity = self.product_quantity + product_quantity_increase
        return self.product_quantity

    def decrease(self, decrease):
        """
        reduces the product by the specified quantity
        parameter : decrease
        return :self.product_quantity
        """
        self.product_quantity = self.product_quantity - decrease
        return self.product_quantity


a = Product("Heets", "cigarettes", 600, 5, "Armenia", "Asia", "Philip Morris", "2017", "summer", 25)
# print(Product.__mro__)
a.present()
print(a.discount(5))
print(a.increase(25))
print(a.decrease(5))
print(a.present())


class Hotel:
    def __init__(self, name, place, mid_room_price, lux_room_price,*args, **kwargs):
        self.name = name
        self.place = place
        self.rooms_mid = {'room1': "free", 'room2': "free", 'room3': "free"}
        self.mid_room_price = mid_room_price
        self.rooms_lux = {'room4': "free", 'room5': "free", 'room6': "free"}
        self.lux_room_price = lux_room_price
        # self.room_mid = self.rooms_mid[self.mid_room_price]
        # self.room_lux = self.rooms_lux[self.lux_room_price]
        super().__init__(*args, **kwargs)

    def presentation_hotel(self):
        return f"name {self.name} place {self.place}\n rooms- " \
               f" rooms middle and rooms \n lux rooms price " \
               f"{self.mid_room_price}(mid) and {self.lux_room_price}(lux)"

    def booking(self, book_room):
        if book_room in self.rooms_mid.keys():
            self.rooms_mid[book_room] = "bussy"
        elif book_room in self.rooms_lux.keys():
            self.rooms_lux[book_room] = "bussy"

    def available_room_check(self, room_type):
        if room_type == "mid":
            if "free" in self.rooms_mid.values():
                for i, k in self.rooms_mid.items():
                    if k == "free":
                        return f"{i} in {k}"
            else:
                return "There is no free room"
        elif room_type == "lux":
            if "free" in self.rooms_lux.values():
                for i, k in self.rooms_lux.items():
                    if k == "free":
                        return f"{i} in {k}"
            else:
                return "There is no free room"

    def discount_room(self, room_name, discount_interest):
        
        if room_name in self.rooms_mid.keys():
            self.rooms_mid[room_name] = \
                self.rooms_mid[room_name]-self.rooms_mid[room_name]*(discount_interest/100)
        elif room_name in self.rooms_lux.keys():
            self.rooms_lux[room_name] = \
                self.rooms_lux[room_name]-self.rooms_lux[room_name]*(discount_interest/100)


class Taxi:
    def __init__(self, name, car_types, price_for_tour, *args, **kwargs):
        self.name_taxi = name
        self.car_types = car_types
        self.price_for_tour = price_for_tour
        super().__init__(*args, **kwargs)

    def presentation_taxi(self):
        return f"name {self.name_taxi}\n type of cars {self.car_types} \n price for trip {self.price_for_tour}"

    def discount_taxi(self, discount_interest):
        self.price_for_tour = \
            self.price_for_tour - self.price_for_tour * (discount_interest / 100)


class Tour(Hotel, Taxi):
    def __init__(self, tour_name, *args, **kwargs):
        self.tour_name = tour_name
        super().__init__(*args, **kwargs)
        self.price_lux = self.mid_room_price + self.price_for_tour
        self.price_mid = self.lux_room_price + self.price_for_tour

    def presentation(self):
        print(f"Hello we offer {self.tour_name} tour we have two options {self.price_lux} and {self.price_mid},\n"
              f"which includes transport with {self.name_taxi} company which provides {self.car_types} cars and "
              f"price for it is {self.price_for_tour},\n"
              f"we will stay at {self.name} which offers two types of rooms middle {self.mid_room_price} "
              f"and lux {self.lux_room_price}")


# d = Hotel("Hotel", "art", "room1", "room5")
# b = Taxi("Hotel_taxi", "BMW", 25000)

c = Tour("Geghart", "Hotel_ARARAT", "Armenia", 10000, 20000, "ride_over", "BMW", 10000)
c.presentation()
# print(d.presentation())
# print(b.presentation_taxi())
# d.booking("room3")
# d.booking("room1")
# d.booking("room2")
# d.booking("room4")
# d.booking("room5")
# d.booking("room6")
# d.discount("room1", 10)
# print(d.rooms_mid)
# print(d.available_room_check("lux"))
