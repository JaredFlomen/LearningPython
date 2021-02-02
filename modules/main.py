from mymodules import generate_full_name, sum_two_num as sum
print(generate_full_name('Jared', 'Flomen'))
print(sum(1, 2))

#Os module
# import os
# os.mkdir('test_directory')

#Sys module
import sys
print('Welcome {}. Enjoy {}'.format(sys.argv[1], sys.argv[2]))