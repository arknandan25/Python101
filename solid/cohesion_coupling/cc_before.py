import string
import random

"""
Every comment I add here is a comment on this code

"""

class VehicleRegistry:
    # this class just looks like a container for these 2 helper methods

    def generate_vehicle_id(self, length):
        return ''.join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id):
        return f"{id[:2]}-{''.join(random.choices(string.digits, k=2))}-{''.join(random.choices(string.ascii_uppercase, k=2))}"


class Application:
    # register_vehicle seems to do a lot of stuff
    # low cohesion that means
    #  has high coupling as it directly relies on VehicleRegistry implementations
    #  if we change VehicleRegistry, then I would have to change register_vehicle
    def register_vehicle(self, brand: string):
        # create a registry instance
        registry = VehicleRegistry()

        """TO MUCH COUPLING HERE, ON methods of VehicleRegistry"""
        # generate a vehicle id of length 12
        vehicle_id = registry.generate_vehicle_id(12)

        # now generate a license plate for the vehicle
        # using the first two characters of the vehicle id
        license_plate = registry.generate_vehicle_license(vehicle_id)


        """
        Weak cohesion is also affected our ability to add a new car, a new if needs to be added
        and we would need to change the if of electric car to make a change there
        
        Also there is coupling b/w brand name and catalogue price
        for electric tax is depending on car brands that currently signify electric, what if we want to add another electric
        brand to our code
        """
        # compute the catalogue price
        catalogue_price = 0
        if brand == "Tesla Model 3":
            catalogue_price = 60000
        elif brand == "Volkswagen ID3":
            catalogue_price = 35000
        elif brand == "BMW 5":
            catalogue_price = 45000

        # compute the tax percentage (default 5% of the catalogue price, except for electric cars where it is 2%)
        tax_percentage = 0.05
        if brand == "Tesla Model 3" or brand == "Volkswagen ID3":
            tax_percentage = 0.02

        # compute the payable tax
        payable_tax = tax_percentage * catalogue_price

        # print out the vehicle registration information
        print("Registration complete. Vehicle information:")
        print(f"Brand: {brand}")
        print(f"Id: {vehicle_id}")
        print(f"License plate: {license_plate}")
        print(f"Payable tax: {payable_tax}")


app = Application()
app.register_vehicle("Volkswagen ID3")
