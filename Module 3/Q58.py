#Q.58 write a python program to read a random line from a file.

fd=open("E:\python_ex\task.py","r")
lines=fd.readlines()
print(random.choice(lines))
fd.close()
