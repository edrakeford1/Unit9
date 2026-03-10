class Restaurant:
    """ Model for a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuising_type = self.cuising_type

    def describe_restaurant(self):
        print(f"The restaurant is named {self.restaurant_name} and it sells {self.cuising_type} food.")

    def open_restaurant(self):
        print(f"{self.restuarant_name} is open for business!")

    chick_fil_a = Restaurant("Chick fil a", "Fast")

    print(chick_fil_a.cuisine_type)
    print(chick_fil_a.restaurant_name)
    
    
