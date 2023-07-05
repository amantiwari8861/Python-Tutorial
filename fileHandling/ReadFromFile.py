
# file1=open("C:/Users/Aman_Tiwari/Desktop/priti.txt","r")
# str1=file1.read()
# print(str1)


# file1=open("C:/Users/Aman_Tiwari/Desktop/priti.txt","r")
# str1=file1.readline()
# print(str1)


file1=open("C:/Users/Aman_Tiwari/Desktop/priti.txt","r")
# str1=file1.readlines()
# print(str1)


# for i in range(len(str1)):
#     print(str1[i])

for l in file1:
    print(l)

file1.close()