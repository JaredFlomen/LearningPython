#Changing tuples to lists
#To modify a tuple, change it to a list
cities = ('Toronto', 'Montreal', 'Vancouver', 'Halifax')
cities = list(cities)
print(cities)
print('Hamilton' in cities)

#Examples
empty_tuple = ()
brothers = ('Adam', 'Kobe')
sisters = ('Sam', 'Jaclyn')
siblings = brothers + sisters
print(siblings)
print(len(siblings))
family = siblings + ('Richard', 'Lisa')
print(family)
print('Kobe' in family)
print('Bingo' in family)