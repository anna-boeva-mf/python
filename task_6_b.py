from sys import argv
from itertools import cycle


script_name, my_str, stop = argv
c = 1
my_list = my_str.split(',')
for i in cycle(my_list):
    print(i)
    c += 1
    if c > int(stop):
        break
