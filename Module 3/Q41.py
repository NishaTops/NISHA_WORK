#Q.41 write a python program to combine two dictionary ading values for common keys.

d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'c':400}
d3={}
for key in d1.keys():
    if key in d2.keys():
        d1[key]=d1[key]+d2[key]
        print(d1)
