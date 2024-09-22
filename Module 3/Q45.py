#Q.45 Write a Python program to find the highest 3 values in a dictionary.

dict = {
    'a': 40,
    'b': 25,
    'c': 99,
    'd': 20,
    'e': 95,
    'f': 45
}
highest_values = sorted(dict.values(), reverse=True)[:3]
print("The highest 3 values are:", highest_values)
