#Day 4
#\n \t \\ \' \"

first_name = 'Jared'
last_name = 'Flomen'
language = 'Python'
formatted_string = 'I am %s %s. I\'m learning %s' % (first_name, last_name, language)
print(formatted_string)

radius = 10
pi = 3.14
area = pi * radius ** 2
formatted_string = 'The area of a circle with a radius %d is %.2f.' % (radius, area)
#2 refers to 2 decimals after the float
print(formatted_string)

#New Formatting
formatted_string = 'I am {} {}. I\'m learning {}'.format(first_name, last_name, language)
print(formatted_string)
formatted_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area)
print(formatted_string)

#String Interpolation
a = 5
b = 4
print(f'{a} + {b} = {a + b}')

#Slicing Strings
language = 'Python'
first_three = language[0:3]
last_three = language[3:6] #Or -3: or 3:
print(last_three)

#Reversing a string
print(language[::-1])

#Capitalize
string_example = 'jared flomen'
print(string_example.capitalize())

#Others: expandtabgs, find, endswith