class Car():
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.mile=0 

  def get_descriptive_name(self):
    long_name = str(self.year) + ' ' + self.make + ' ' + self.model
    return long_name.title()
  def read_mile(self):
    print('This car has ran ',self.mile, 'miles')
  def update_mile(self,mile_ran):
    if mile_ran >= self.mile:
      self.mile=mile_ran
    else:
      print('what are you doing dude, you can not roll back an odometer !')
  def increase_mile(self,mile_more):
    if mile_more <= 0:
      print('You can not roll back an odometer !')
    else:
      self.mile=self.mile+ mile_more
      self.mile+=mile_more
      #多用下这种方法！！！
  def fill(self):
    print('yes')


class Battery():
  def __init__(self,battery_size=90):
    self.battery_size=battery_size 
  def describe_battery(self):
    print('This is a ',str(self.battery_size),' kWh battery !')
  def get_range(self):
    range=0
    if self.battery_size==70:
      range=240
    elif self.battery_size==85:
      range=270
    message='This car can go approximately '+str(range)+' miles on a full charge.'
    print(message)



class ElectricCar(Car):
  def __init__(self,make,model,year):
    super().__init__(make,model,year)
    self.battery=Battery(85)

mytesla=ElectricCar('tesla','model s','2022')
print(mytesla.get_descriptive_name())
mytesla.battery.describe_battery()
mytesla.battery.get_range()