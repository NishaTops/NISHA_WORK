#Q.47Write a Python program to create a dictionary from a string.


string = "w3resource"


dict = {}


for char in string:
    if char in dict:
        dict[char] += 1 
    else:
        dict[char] = 1
print(dict)
