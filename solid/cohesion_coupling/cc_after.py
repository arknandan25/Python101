import string
import random

"""
* Try to separate information:
 - brand information
 - vehicle id
Center your code around your data

This code has high cohesion(i.e a piece of code only does one thing)
and low coupling (i.e one class stuff not depending too much on another class)
"""
#  these classes signify the data we would deal with


class VehicleInfo:
    def __init__(self, brand: str, catalogue_price: int, electric: bool):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.electric = electric

    def calculate_tax(self):
        tax_percentage = 0.05
        if self.electric:
            tax_percentage = 0.02
        return tax_percentage * self.catalogue_price

    def print(self):
        print(f" Brand: {self.brand}")
        print(f" Tax: {self.calculate_tax()}")


class Vehicle:
    def __init__(self, vehicle_id: str, vehicle_license: str, vehicle_info: VehicleInfo):
        self.vehicle_id = vehicle_id
        self.vehicle_license = vehicle_license
        self.vehicle_info = vehicle_info

    def print(self):
        print(f"vehicle id: {self.vehicle_id}")
        print(f"vehicle license: {self.vehicle_license}")
        self.vehicle_info.print()


class VehicleRegistry:
    vehicle_mapping = {}

    def __init__(self):
        # I personally donot feel this is the best approach here
        # also maintaining the vehicle_mapping as a class var, but for now its a better approach then the previous one
        self.add_brand("Tesla Model 3", 60000, True)
        self.add_brand("Volkswagen ID3", 35000, True)
        self.add_brand("BMW 5", 45000, False)

    def add_brand(self, brand, catalogue_price, electric):
        self.vehicle_mapping[brand] = VehicleInfo(brand, catalogue_price, electric)

    def create_vehicle(self, brand, length=12):
        # referring to a class method via self is not coupling
        vehicle_id = self.generate_vehicle_id(length)
        vehicle_license = self.generate_vehicle_license(vehicle_id)
        return Vehicle(vehicle_id, vehicle_license, self.vehicle_mapping[brand])

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:
    def register_vehicle(self, brand: string):
        """Register should not print, that customers resposibility, we just have to give them tthe ability to do so"""

        registry = VehicleRegistry()
        return registry.create_vehicle(brand)


app = Application()
vehicle = app.register_vehicle("Tesla Model 3")
vehicle.print()
