#Q.28 write a python program to remove an empty tuple(s) from a list of a tuple.

L=[(),(),('',),('a','b'),('a','b','c'),('d')]
L=[t for t in L if t]
print(L)


