#Lists

lst = ['Leafs', 'Habs', 'Sens', 'Oilers', 'Flames']
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