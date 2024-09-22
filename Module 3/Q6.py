#Q.6 write a python program to count the program of strings where the string length is 2 or more and the first and last character 
#are same from a given list of strings.
s=0
list1=["defe","efe","nsn","eft"]
for x in list1:
    if len(x)>1 and x[0]==x[-1]:
        print(x)
        s=s+1
        print(s)
        




