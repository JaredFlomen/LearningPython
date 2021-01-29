first_name = 'Jared'
last_name = 'Flomen'
country = 'Canada'
city = 'Toronto'
age = 26
is_married = False
skills = ['React', 'Ruby on Rails', 'JS']
person_info = {
  'firstname': 'Jared',
  'lastname': 'Flomen',
  'country': 'Canada',
  'city': 'Toronto'
}

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

first_name, last_name, country, age, is_married = 'Adam', 'Flomen', 'Canada', 23, False
print(first_name, last_name, country, age, is_married)

first_name = input('What is your name')
age = input('How old are you?')
print(first_name)
print(age)