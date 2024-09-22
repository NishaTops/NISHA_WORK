#Q.49Write a Python function to check whether a number is in a given range.

def rang(num, start, end):
    if start <= num <= end:
        return True
    else:
        return False


print(rang(55, 1, 10))    
print(rang(18, 1, 10 ))
print(rang(8, 1, 5))    
print(rang(15, 1, 20))   

