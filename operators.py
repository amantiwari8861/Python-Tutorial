# 5+2 here + is operator and 5 and 2 are operands

# binary (bi ->2 )
    #arithematic operator eg. +,-,*,/,**,%
# num1=2
# num2=5
# num3=num1+num2 # 2+5 =7
# num3=num1-num2 # 2-5 =-3
# num3=num1*num2 # 2*5 =10
# num3=num1/num2 # 0.4
# num3=num1**num2  #2*2*2*2*2 =32 for power
# num3=num1%num2 # 2
# num3=27%4 # for remainder
# print("the result is ",num3)
    
    #relational operator eg. <,>, <=,>=,== ,!=
var1=340
var2=56
# res=var1<var2
# res=var1>var2
# res=12<=12   #true
# res=12>=12
# res=15==10
# res=15==15
# res= 15!=15
# print("The statement is ",res)


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

print(10&7)
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


print(10<<1) #left shift
# # 10*2
print(10<<2) #left shift
# # 10*2*2
print(10<<3) #left shift
# 10*2*2*2

print(128>>1) #right shift
# 128/2 -> 64
print(128>>2) #right shift
# (128/2)/2 -> 32
print(128>>3) #right shift
# ((128/2)/2)/2 -> 16
# ----------------------------------------------------------------
#identity operators
# name="Aman Tiwari"
# name2="Aman Tiwari"
# print(name is name2)
# print(name is not name2)

# membership operators
# name3="hello everyone"
# print('no' in name3)
# print('hello' not in name3)

#ternary operator (conditional operator)

# num=int(input("enter num1 \n")) #\n for new line
# num=int(input("enter num1 \n")) #\n for new line
# num2=int(input("enter num2 \t")) #\t for tabular space (tab)

# min=num if num<num2 else num2
# print("the minimun is ",min)
# max=num if num>num2 else num2
# print("the maximum is ",max)

# print("hello",end="\t")
# print("h","e","l",sep="@")
