#Q.3 Differentiate between append()and extend()methods?

#append add a single element to  the end of list.

colours=["red","green","blue"]
colours.append("yellow")
print(colours)


#extend add element from an iterable to the end of a list.

L=["black","orange"]
colours.extend(L)
print(colours)
