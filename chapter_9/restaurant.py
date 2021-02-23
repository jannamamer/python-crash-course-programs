class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describe the restaurant"""
        print(f"Restaurant name: {self.restaurant_name}")
        print(f"Cuisine type: {self.cuisine_type}")
        print(f"Number served: {self.number_served}")

    def open_restaurant(self):
        """Show message that restaurant is open."""
        print(f"\n{self.restaurant_name} is now open!")

    def set_number_served(self, number_served):
        """Update the number server by the given value"""
        if number_served >= self.number_served:
            self.number_served = number_served
        else:
            print("You cannot roll back a served number.")


restaurant = Restaurant("Lab 151", "Thai")
restaurant.open_restaurant()
restaurant.describe_restaurant()

restaurant.number_served = 5
restaurant.describe_restaurant()

restaurant.set_number_served(10)
restaurant.describe_restaurant()
