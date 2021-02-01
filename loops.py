count = 0
while count < 5:
  if count == 3:
    break
  print(count)
  count = count + 1
print('end')

numbers = [0, 1, 2, 3, 4]
for number in numbers:
  print(number)

person = {
  'first_name': 'Jared',
  'last_name': 'Flomen',
  'age': 25,
  'country': 'Canada',
  'skills': ['Javascript', 'React', 'Python', 'Ruby']
}

for key, value in person.items():
  print(key, value)

numbers = (1, 2, 3, 4, 5)
for number in numbers:
  print(number)
  if number == 3:
    continue
  print('Next number should be ', number + 1) if number != 5 else print('Loop\'s end')
print('Outside the loop')

for number in range(11):
  print(number)
else:
  print('The loop stops at', number)

#Loop that makes 7 calls to print, output a triangle
hashtag = '#'
while len(hashtag) < 8:
  print(hashtag)
  hashtag += '#'

#Sum of all numbers between 0 to 100
counter = 0
for number in range(101):
  counter += number
else:
  print('The sum of all numbers is ', counter)