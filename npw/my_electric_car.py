from electricar import ElectricCar as EC 
from electricar import Car 
my_tesla= EC('tesla','model s',2022)
print(my_tesla.get_descriptive_name())
my_tesla.read_mile()
my_tesla.mile=28
my_tesla.read_mile()
my_tesla.increase_mile(89)
my_tesla.read_mile()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

my_audi=Car('audi','a4',2022)
print(my_audi.get_descriptive_name())