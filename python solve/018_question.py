class Building:
    def __init__(self, address, contractor, age, floors):
        self.details = {
            "address": address,
            "contractor": contractor,
            "floors": floors,
            "age": age
        }

    def get_address(self): return self.details["address"]

    def get_contractor(self): return self.details["contractor"]

    def get_age(self): return self.details["age"]

    def get_floors(self): return self.details["floors"]

    def printDetails(self):
        print("***** Building Details *****")
        for k, v in self.details.items():
            print(k, ":", v)

        print()


class Apartment(Building):
    def __init__(self, name, address, contractor, residents, age, floors):
        super().__init__(address, contractor, age, floors)

        self.details["name"] = name
        self.details["residents"] = residents


class House(Building):
    def __init__(self, owner, address, contractor, age, floors):
        super().__init__(address, contractor, age, floors)

        self.details["owner"] = owner


class Commercial(Building):
    def __init__(self, name, address, building_type, contractor, age, floors):
        super().__init__(address, contractor, age, floors)

        self.details["name"] = name
        self.details["type"] = building_type


apt = Apartment("Diwas", "Chahabel", "JC Constructions", 34, 15, 25)
home = House("Raj", "Sifal", "JC Constructions", 5, 3)
com = Commercial("Hayat", "Chhauni", "Hotel", "JC Constructions", 25, 45)

apt.printDetails()
home.printDetails()
com.printDetails()
