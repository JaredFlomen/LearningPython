def square(x):
  return x ** 2

def cube(x):
  return x ** 3

def absolute(x):
  if x >= 0:
    return x
  else:
    return - (x)

def higher_order_function(type):
  if type == 'square':
    return square
  elif type == 'cube':
    return cube
  elif type == 'absolute':
    return absolute

result = higher_order_function('square')
print(result(3))

result = higher_order_function('cube')
print(result(2))

#Python Closures
def add_ten():
  ten = 10

  def add(num):
    return num + ten
  return add

closure_result = add_ten()
print(closure_result(20))

#Python Decorators
def uppercase_decorator(function):
  def wrapper():
    func = function()
    make_uppercase = func.upper()
    return make_uppercase
  return wrapper
@uppercase_decorator
def greeting():
  return 'Jared is learning Python'
print(greeting())

#Built in higher order functions
#Map
numbers = [1, 2, 3]
def squared(x):
  return x ** 2

nums_squared = map(squared, numbers)
print(list(nums_squared))

squared_with_lambda = map(lambda x: x ** 2, numbers)
print(list(squared_with_lambda))

names = ['Jared', 'Adam', 'Josh']
def upper(name):
  return name.upper()
print(list(map(upper, names)))

#Filter
numbers = [1, 2, 3, 4, 5]
def check_even(num):
  if num % 2 == 0:
    return True
  return False
even_numbers = filter(check_even, numbers)
print(list(even_numbers))