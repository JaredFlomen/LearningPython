def generate_name ():
    first_name = 'Jared'
    last_name = 'Flomen'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_name ()

#Returning a value
def generate_full_name ():
    first_name = 'Jared'
    last_name = 'Flomen'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

#Functions with parameters
def add_ten(num):
  ten = 10
  return num + ten
print(add_ten(20))

def sum_of_numbers(n):
  total = 0
  for i in range(n + 1):
    total += i
  print(total)
sum_of_numbers(5)

def calcualte_age(current_year, birth_year):
  age = current_year - birth_year
  return age
print('Age: ', calcualte_age(2021, 1994))

#Returning a list
def find_even_numbers(n):
  evens = []
  for i in range(n + 1):
    if i % 2 == 0:
      evens.append(i)
  return evens
print(find_even_numbers(10))

#Passing default values
def greetings(name='Adam'):
  message = name + ', is learning to code'
  return message
print(greetings())
print(greetings("Jared"))

#Arbitrary number of arguments
def arb_args(*args):
  total = 0
  for num in args:
    total += num
  return total
print(arb_args(1, 2, 3, 4))