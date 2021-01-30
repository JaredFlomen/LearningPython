print('Addition: ', 1 + 2)
print('Division without the remainder: ', 7 // 2)
print('Moduus: ', 3 % 2)
print('Division without the remainder: ', 7 // 3)
print('Exponential: ', 3 ** 2)

a = 3
b = 2

total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponential = a ** b

print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponential)

#Calculating area of a circle
radius = 10
area_of_circle = 3.14 * radius ** 2
print('Area of circle: ', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')

#Comparison Operators
print(len('mango') != len('avocado'))
print(len('mango') == len('avocado'))

#Is, Is Not, In, Not In
print('coding' in 'coding for all')
print('2 is not 3', 2 is not 3)
print('J in Adam', 'J' in 'Adam')

base = int(input('Enter base: '))
height = int(input('Enter height: '))
area = 0.5 * base * height
print('The area of the triangle is ', area)

hours = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
earnings = hours * rate
print('Your weekly earnings is ', earnings)