from sys import argv
from itertools import count


script_name, start, stop = argv
for i in count(int(start)):
    if i > int(stop):
        break
    else:
        print(i)
