# [cont.] Have to write a class called IceCreamStand that inherits from,
# the Restaurant class from Ex 3. Add an attribute called flavors that,
# store a list of ice cream flavors. Write a method that displays these,
# flavors.
# Create an instance of IceCreamStand, and call this method.

class Restaurant:
    """A simple class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Information about the restaurant."""
        print(f"\n{self.restaurant_name} is the best restaurant in town.")
        print(f"The restaurant offers {self.cuisine_type} food.")

    def open_restaurant(self):
        """Restaurant opening times message."""
        print(f"The {self.restaurant_name} is open from 9am to 5pm.")

    def customer_number(self):
        """Print the number of customers the restaurant has served."""
        print(f"{self.number_served} customers have been served.")

    def set_number_served(self, new_number):
        """Set the number of customers"""
        self.number_served = new_number

    def increment_number_served(self, new_number):
        """Increment the number of customers."""
        self.number_served += new_number

class IceCreamStand(Restaurant):
    """An ice cream stand class that inherits from the Restaurant class."""

    def __init__(self, restaurant_name, cuisine_type, flavors):
        # flavors = ['vanilla', 'chocolate', 'strawberry']
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        print("\nThe flavors available are:")
        for flavor in self.flavors:
            print(f"-{flavor.title()}")

ice_cream_flavors = IceCreamStand('Golden Valley', 'Fish',['vanilla', 'chocolate', 'strawberry'])
ice_cream_flavors.display_flavors()

# Creating an instance of the Restaurant class.
restaurant = Restaurant('Golden Valley', 'Fish')

print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 10
restaurant.customer_number()

restaurant.set_number_served(30)
restaurant.customer_number()

restaurant.increment_number_served(10)
restaurant.customer_number()

