class Restaurant:
    """ Model for a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The restaurant is named {self.restaurant_name} and it sells {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open for business!")

chick_fil_a = Restaurant("Chick fil a", "Fast")

print(chick_fil_a.cuisine_type)
print(chick_fil_a.restaurant_name)
print(chick_fil_a.describe_restaurant())
print(chick_fil_a.open_restaurant())