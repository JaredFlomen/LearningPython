class Person:
  def __init__(self, firstname, lastname, age, country, city):
    self.firstname = firstname
    self.lastname = lastname
    self.age = age
    self.country = country
    self.city = city
  
  def person_info(self):
    return f'{self.firstname} {self.lastname} lives in {self.city}'

p = Person('Jared', 'Flomen', 26, 'Canada', 'Toronto')
print(p.firstname)
print(p.city)
print(p.person_info())