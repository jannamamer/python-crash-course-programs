class User:
    """Represents a user"""

    def __init__(self, first_name, last_name, middle_name=''):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name

    def describe_user(self):
        print("\nUser information")
        print(f"\tFirst name: {self.first_name}")
        print(f"\tLast name: {self.last_name}")

        if self.middle_name:
            print(f"\tMiddle name: {self.middle_name}")

    def greet_user(self):
        print(f"Hi, {self.first_name} {self.last_name}")


my_user = User("Janna", "Dela Cruz", "Ureta")
my_user.describe_user()
my_user.greet_user()

other_user = User("Mamer", "Dela Cruz")
other_user.describe_user()
other_user.greet_user()
