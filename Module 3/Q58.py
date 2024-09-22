#Q.58 write a python program to read a random line from a file.

import random

fd=open("nisha.txt","r")
lines=fd.readlines()
print(random.choice(lines))
fd.close()
