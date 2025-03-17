# A class called User which stores a person's personal information

class User:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    # Methods to print user information
    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name} and I am {self.gender.lower()} aged {self.age}")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

user1 = User('Fatima', 'Gerald', 21, 'Female')
user1.describe_user()
user1.greet_user()

