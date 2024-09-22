#Q.64Write a Python program to find the maximum and minimum numbers from the specified decimal numbers. 
decimal_numbers=[3.5,8.6,1.7,6.7,4.4]
if decimal_numbers:
    max_numbers=max(decimal_numbers)
    min_number=min(decimal_numbers)
    print(f"Maximum number:{max_numbers}")
    print(f"Minimum number:{min_number}")
else:
    print("The list is empty.")

