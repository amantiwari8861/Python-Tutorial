""" i=1
while i<= 10:
    print(" i =",i)
    # i=i+1
    i += 1 """

""" i=1
while i<= 10:
    print(" i =",i)
    # i=i+1
    i += 1
else:
    print(" i's value exceeds from 10 i.e i =",i)
 """

# Loop control statements
#break
""" a=1
while(a <= 100):
    print("a =",a)
    a+=1
    if a==50:
        break """

#continue
a=0
while(a < 10):
    a+=1
    if a==5:
        print(" skipping the 5th step")
        continue
    print("a =",a)   