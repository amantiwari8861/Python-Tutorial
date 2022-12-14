#logical operators
#and, or, not

#and (both the conditions must be satisfied)
print( 10>5 and 10<20 ) # True and True -> True
print( 10>5 and 10<5 ) # True and False -> False
print( 10>50 and 10<50 ) # False and True -> False
print( 1>5 and 10<5 ) # False and False -> False

# # #or (at least one of the conditions must be satisfied)
print( 10>5 or 10<20 ) # True and True -> True
print( 10>5 or 10<5 ) # True or False -> True
print( 10>50 or 10<50 ) # False and True -> True
print( 1>5 or 10<5 ) # False and False -> False

# # #not (complement of the output)
print(not 10>5) # not True -> False
print(not 10>50) # not False -> True