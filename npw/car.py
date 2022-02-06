class Car():
  '''a class describe cars'''
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
      
      self.mile+=mile_more
      #多用下这种方法！！！

