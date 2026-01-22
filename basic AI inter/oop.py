# Define the class
class Car:
    def __init__(self, brand, model, year, millage):
        self.brand = brand
        self.model = model
        self.year = year
        self.millage = millage
    # Method to print car details
    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year},Millage:{self.millage} km/l")

# Create two car objects
car1 = Car("Toyota", "Corolla", 2020,17.5)
car2 = Car("Honda", "Civic", 2022,15.3)

# Call car_info() method for each
car1.car_info()
car2.car_info()
