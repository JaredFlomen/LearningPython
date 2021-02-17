import copy

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Company:
  def __init__(self, boss, employee):
    self.boss = boss
    self.employee = employee

p1 = Person("Jared", 26)
p2 = Person('Adam', 20)

# p2.age = 28

# print(p2.age)
# print(p1.age)

company = Company(p1, p2)
company_clone = copy.copy(company)

company_clone.boss.age = 27
print(company_clone.boss.age)
print(company.boss.age)