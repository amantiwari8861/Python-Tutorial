#logical operators
#and, or, not

#and (both the conditions must be satisfied)
# print( 10>5 and 10<20 ) # True and True -> True
# print( 10>5 and 10<5 ) # True and False -> False
# print( 10>50 and 10<50 ) # False and True -> False
# print( 1>5 and 10<5 ) # False and False -> False

# # # #or (at least one of the conditions must be satisfied)
# print( 10>5 or 10<20 ) # True and True -> True
# print( 10>5 or 10<5 ) # True or False -> True
# print( 10>50 or 10<50 ) # False and True -> True
# print( 1>5 or 10<5 ) # False and False -> False

# # # #not (complement of the output)
# print(not 10>5) # not True -> False
# print(not 10>50) # not False -> True

# Logical or

marks=int(input("enter marks"))
if marks>=90 or marks<=100:
    print("Got A1 Grade!!")

#    case 1: marks=38
#             38>=90 or 38<=100
#             False or True 
#             True

#    case 2: marks=95
#             95>=90 or 95<=100
#             True or True 
#             True

#    case 3: marks=120
#             120>=90 or 120<=100
#             True or False 
#             True

# Logical and

# marks=int(input("enter marks"))
# if marks>=90 and marks<=100:
#     print("Got A1 Grade!!")

#    case 1: marks=38
#             38>=90 and 38<=100
#             False and True 
#             False

#    case 2: marks=95
#             95>=90 and 95<=100
#             True and True 
#             True

#    case 3: marks=120
#             120>=90 and 120<=100
#             True and False 
#             False