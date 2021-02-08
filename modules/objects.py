class Person:
  def __init__(self, firstname, lastname, age, country, city):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city

p = Person('Jared', 'Flomen', 26, 'Canada', 'Toronto')
print(p.firstname)
print(p.city)