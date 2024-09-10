#Q.46 wrie a python program to combine values in python list of dictionaries

from collections import Counter

# Sample data
data = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]

# Create a Counter object to accumulate amounts
counter = Counter()

# Iterate through each dictionary in the list
for entry in data:
    item = entry['item']
    amount = entry['amount']
    counter[item] += amount

# Print the result
print("Counter", dict(counter))

