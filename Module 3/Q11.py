#Q11 Write a Python function that takes a list and returns a new list with uniqueelements of the first list. 
def uniq_ele(input_list):
    return list(set(input_list))


input_list = [1, 2, 2, 3, 4, 4, 5]
uniq_list = uniq_ele(input_list)
print(uniq_list)
