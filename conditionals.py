a = -1
if a > 0:
  print('A is a positive number')
elif a < 0:
  print('A is a negative number')
else:
  print('A is zero')

b = -1
print('B is positive') if b > 0 else print('B is negative')

a = 3
if a > 0 and a % 2 == 0:
  print('A is an even and positive integer')
elif a > 0 and a % 2 != 0:
  print('A is a positive integer')
elif a == 0:
  print('A is zero')
else:
  print('A is negative')

#IF and OR
user = 'Jared'
access_level = 4

if user == 'admin' or access_level >= 4:
  print('Access granted!')
else:
  print('Access denied!')

age = int(input('How old are you: '))
if age > 16:
  print('You are old enough to drive')
else:
  years_to_drive = 16 - age
  print(f'You need {years_to_drive} more years to learn to drive')