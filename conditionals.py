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
access_level = 3

if user == 'admin' or access_level >= 4:
  print('Access granted!')
else:
  print('Access denied!')