#Q.10 write a python program to generate  and print a list of first and last 5 elements where the values are square of numbers
#between 1 and 30.

squares=[i**2 for i in range(1,31)]
first_five=squares[:5]
last_five=squares[-5:]
print("first 5 elements:",first_five)
print("last 5 elements:",last_five)


