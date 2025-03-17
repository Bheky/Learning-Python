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
my_fave_dog.sit()
my_fave_dog.roll_over()

print(f"My do's name is {my_fave_dog.name}.")
print(f"He is {my_fave_dog.age} years old.")

