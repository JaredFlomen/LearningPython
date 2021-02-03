even_numbers = [i for i in range(21) if i % 2 == 0]
print(even_numbers)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive__and_even = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive__and_even)

#Lambda function
add_numbers = lambda a, b: a + b
print(add_numbers(1, 2))
#Self invoking lambda
print((lambda a, b: a + b)(2, 3))

#Lambda inside another function
def power(x):
  return lambda n: x ** n
cube = power(2)(3)
print(cube)

list_of_lists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
filter_numbers = [item for sublist in list_of_lists for item in sublist]
filter_twice = [items for sublist in filter_numbers for items in sublist]
print(filter_twice)