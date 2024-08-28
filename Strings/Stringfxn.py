str1="the quick.BRown fox JUMPS over the lazy frog Fox  fox"
# length=len(str1)
# print("the sentence length is ",length)
# print(len(str1))
# print(str1[4])
# print(str1[4:9]) # here 9th index is not included
# print(str1[0:9])
# print(str1[:9])
# print(str1[-1])
# print(str1[-2:-1])
# print(str1[-6:0]) # won't work
# print(str1[-6:])
# df[start:stop:step]
# print(str1[-4:1:-1]) # to reverse a string
# print(str1[::3]) 
# print(str1[::2])
# print(str1[::-2])
# print(str1[-2])
# print(str1[-8:-2])
# print(str1[::2])
# print(str1[4::2])
# print(str1[::-2])
# print(str1[::-1])
# print(str1.lower())
# print(str1.upper())
# print(str1.title())
# print(str1.capitalize())
# print(str1.find("fox"))
# print(str1.islower())
# print(str1.count("fox"))
# print("@".join("Hii"))
# strarr=str1.split(" ")
# print(strarr)
# print("-".join(strarr))
# print(" ".join(strarr))
# print("_".join(strarr))


# print("".join(["aman","ram","shyam"]))
# print("_".join(["aman"]))
# print("_".join("Aman"))

# result="_".join(["aman","ram","shyam"])
# print(result)
# result="aman_ram_shyam"
# listOfNames=result.split("_")
# print(listOfNames)

# print(len("     Aman   ".strip()))
# print(len("     Am       an   ".rstrip()))
# print(len("     Am       an   ".strip()))


newStr=""
for i in "     Am       an   ":
    if ord(i) != 32:
        newStr+=i

print(newStr)



# newStr="Aman@123"
# newTwo=""
# for i in newStr:
#     if ord(i)>=97 and ord(i)<=122:
#         newTwo+= chr(ord(i)-32)
#     else:
#         newTwo+=i
# print(newTwo)

