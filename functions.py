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
