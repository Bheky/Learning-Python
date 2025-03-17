# Cont. from the Restaurant class exercise,
# add an attribute called number_served with a default value of 0.
# Create an instance called restaurant from this class.
# Print the number of customers the restaurant has served, and then change this value,
# and print it again.
# Add a method called set_number_served() that lets you set the number of
# customers that have been served. Call this method with a new number and print
# the value again.
# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a day of
# business.

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

# Creating an instance of the Restaurant class.
restaurant = Restaurant('Golden Valley', 'Fish')

# Printing attributes
#print(f"Restaurant name: {restaurant.restaurant_name}")
#print(f"Cuisine type: {restaurant.cuisine_type}")

print(f"Number of customers served: {restaurant.number_served}")

restaurant.number_served = 10
restaurant.customer_number()

restaurant.set_number_served(30)
restaurant.customer_number()

restaurant.increment_number_served(10)
restaurant.customer_number()

# Calling methods
#restaurant.describe_restaurant()
#restaurant.open_restaurant()

