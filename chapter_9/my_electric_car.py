from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', '2019')

print(my_tesla.get_desriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
