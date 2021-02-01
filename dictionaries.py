#A collection of unordered, modifiable paired data

person = {
  'first_name': 'Jared',
  'last_name': 'Flomen',
  'age': 25,
  'country': 'Canada',
  'skills': ['Javascript', 'React', 'Python', 'Ruby']
}

print(len(person))
print(person['first_name'])
print(person['skills'][2])
print(person.get('city'))
person['city'] = 'Toronto'
person['skills'].append('Rails')
person['age'] = 26
print(person)