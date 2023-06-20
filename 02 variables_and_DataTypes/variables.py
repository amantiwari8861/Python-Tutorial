# variable is a special type of containers which is used  to store the data into them

# num=56   #valid name
# print("num")
# print(num)

# num value=54 #invalid name because of space in between
# print(num value)

# 9num=78 #invalid name bcz numeric value is not allowed in the beginning
# print(9num)

# $num=96 #invalid name bcz no special character is allowed except underscore (_)
# print($num)

# import=20 #import is a pre-defined keyword in python
# print(import)

import keyword
print(keyword.kwlist)
print("there are ",len(keyword.kwlist)," keywords in python")
