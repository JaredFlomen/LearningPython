#Set is a colleciton of unordered and unindexed distinct elements

planets = {'earth', 'mars', 'venus', 'jupiter'}
planets.add('saturn')
print(planets)

#Can use update as well
friends = {'Dean', 'Lewis', 'Billy', 'earth'}
combined_list = planets.union(friends)
print(combined_list)

#Intersection
intersection = friends.intersection(planets)
print(intersection)

#Checking difference between two sets
print(planets.difference(friends))