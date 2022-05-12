# print("hello in python")
""" '''print("multiple")
print("line")
print("comment")'''
print("hello in python")
print('hii')
print("hello in python")
print("hello in python") """

#variables
#variables are containers for storing data
""" num=10
print(type(num))
name='Aman Tiwari'
print(type(name))
pi=3.14
print(type(pi)) """


#operators
# 5+4  5 and 4 are called operands and + is called operator

""" num1,num2=27,5
num3=num1+num2
print(num3)

num4=num1-num2
print(num4)

num5=num1*num2
print(num5)

num6=num1/num2
print(int(num6))

num7=num1%num2  #modulus (to find the remainder)
print(num7)

num8=5**2 #5 to the power of 2
print(num8) """

#relational operators
#eg. >,<,==,!=,>=,<=
# print(10!=10)

#logical operators
#and, or, not

#and (both the conditions must be satisfied)

# print( 10>5 and 10<20 ) # true and true -> true
# print( 10>5 and 10<5 ) # true and false -> false
# print(not 10>5) # not true -> false

# #or (at least one of the conditions must be satisfied)
# print( 10>5 or 10<5 ) # true or false -> true

#assignment operators (shorthand operators)
# eg. =,+=, -=, *=, /=, %=, **=

# num9=56

# num9+=10 #same as num9=num9+10 -> num9=66
# print(num9)


#bitwise operators
# eg. &, |, ^, >>, <<

# print(10&7)
# 10 -> 1010
# 7 ->  0111
#10&7 -> 0010 -> 2

# print(10|7)
# 10 -> 1010
# 7 ->  0111
#10|7 ->  1111 -> 15

# print(10^7) # same bits become zero
# 10 -> 1010
# 7 ->  0111
# 10^7 -> 1101 -> 13


# print(10<<1) #left shift
# # 10*2
# print(10<<2) #left shift
# # 10*2*2
# print(10<<3) #left shift
# 10*2*2*2

# print(128>>1) #right shift
# 128/2 -> 64
# print(128>>2) #right shift
# (128/2)/2 -> 32
# print(128>>3) #right shift
# ((128/2)/2)/2 -> 16
