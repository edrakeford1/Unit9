class Restaurant:
    """ Model for a restaurant"""
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Printing name of restaurant and what it sells """
        print(f"The restaurant is named {self.restaurant_name} and it sells {self.cuisine_type} food.")

    def open_restaurant(self):
        """ Printing restaurant is open """
        print(f"{self.restaurant_name} is open for business!")

    def set_number_served(self, number):
        """ Set number of customers served """
        self.number_served = number

    def increment_number_served(self, number):
        """ Increment number of customers served in a day """
        self.number_served += number

chick_fil_a = Restaurant("Chick fil a", "Fast")

chick_fil_a.increment_number_served(5)
chick_fil_a.increment_number_served(5)
chick_fil_a.increment_number_served(5)
print(chick_fil_a.number_served)
chick_fil_a.set_number_served(0)
print(chick_fil_a.number_served)

