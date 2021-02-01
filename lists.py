#Lists

lst = ['Leafs', 'Habs', 'Sens', 'Oilers']
first_item, second_item, third_item, *rest = lst
print(first_item)
print(second_item)
print(third_item)
print(rest)

#Checking items in a list
does_exist = 'Knights' in lst
print(does_exist)

#Adding items to a list
lst.append('Cacucks')
print(lst)

#Inserting into a list
lst.insert(2, 'Flames')
print(lst)

#Delete
del lst[1]
print(lst)

#Join using extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print(num1)