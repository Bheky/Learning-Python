# A simple class to represent a pet in this instance a dog

# Define the class called Dog
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Calling methods
my_fave_dog = Dog('Speaf', 5)
your_dog = Dog('Bruno', 8)

print(f"My dog's name is {my_fave_dog.name}.")
print(f"He is {my_fave_dog.age} years old.")
my_fave_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"He is {your_dog.age} years old.")
your_dog.roll_over()
