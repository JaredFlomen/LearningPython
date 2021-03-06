from mymodules import generate_full_name, sum_two_num as sum
print(generate_full_name('Jared', 'Flomen'))
print(sum(1, 2))

#Os module
# import os
# os.mkdir('test_directory')

#Sys module
# import sys
# print('Welcome {}. Enjoy {}'.format(sys.argv[1], sys.argv[2]))

#Statistics module
from statistics import mean, median, mode, stdev
ages = [10, 12, 16, 18, 20, 24, 26]
print('Statistics module')
print(mean(ages))
print(median(ages))
print(mode(ages))
print(stdev(ages))

#Math module
import math
print('Math module')
print(math.floor(128.21))

#Random module
from random import random, randint
print('Random module')
print(random()) #Between 0 and 0.999
print(randint(5, 20)) #Between args passed