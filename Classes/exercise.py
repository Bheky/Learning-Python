# A class called Restaurant which stores two attributes.
# Then use a method to print information about the restaurant and another method,
# to print a message indicating that the restaurant is open.
# Note: Make an instance called restaurant from your class. Print the two attributes individually,
# and then call both methods.

class Restaurant:
    """A simple class representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Information about the restaurant."""
        print(f"\n{self.restaurant_name} is the best restaurant in town.")
        print(f"The restaurant offers {self.cuisine_type} food.")

    def open_restaurant(self):
        """Restaurant opening times message."""
        print(f"The {self.restaurant_name} is open from 9am to 5pm.")

# Creating an instance of the Restaurant class.
restaurant = Restaurant('Golden Valley', 'Fish')

# Printing attributes
print(f"Restaurant name: {restaurant.restaurant_name}")
print(f"Cuisine type: {restaurant.cuisine_type}")

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
