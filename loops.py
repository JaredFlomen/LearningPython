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