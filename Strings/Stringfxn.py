str1="the quick.brown fox jumps over the lazy frog"

# length=len(str1)
# print("the sentence length is ",length)
print(len(str1))
print(str1[4])
print(str1[4:9])
print(str1[0:9])
print(str1[:9])
print(str1[-2])
print(str1[-8:-2])
print(str1[::2])
print(str1[4::2])
print(str1[::-2])
print(str1.lower())
print(str1.upper())
print(str1.title())
print(str1.capitalize())
print(str1.find("fox"))
print(str1.islower())
print(str1.count("fox"))
print("@".join("Hii"))
strarr=str1.split(" ")
print(strarr)
print("@".join(strarr))