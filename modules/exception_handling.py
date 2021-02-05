try:
  name = input('Enter your name: ')
  year_born = input('What year born: ')
  age = 2021 - int(year_born)

  print(f'You are {name}. And you are {age} years old')

except TypeError:
  print('Type error occurred')
except ValueError:
  print('Value error occurred')
except ZeroDivisionError:
  print('Zero division error occurred')

else:
  print('I usually run with a try block')
finally:
  print('I always run')

#Unpacking dictionaries
def unpacking_dictionaries(name, country, city, age):
  return f'{name} lives in {country}, {city}. He is {age} years old'

person = {'name': 'Jared', 'country': 'Canada', 'city': 'Toronto', 'age': 27}
print(unpacking_dictionaries(**person))