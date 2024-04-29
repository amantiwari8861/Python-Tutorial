# file1=open("C:\\Users\\admin\\Desktop\\helloPy.txt","r")
# str1=file1.read()
# print(str1)
# print("i will run after reading file")
# print("i will run after reading file")
# print("i will run after reading file")
# print("i will run after reading file")
# file1=None
# try:
#     file1=open("C:\\Users\\admin\\Desktop\\helloPy.txt","r")
#     str1=file1.read()
#     print("The Content in File is :\n",str1)
# except FileNotFoundError:
#     print("File doesn't exist!!")
# except:
#     print("unable to open file may be u don't have permissions to open file\n or file is corrupted")
# finally:
#     print("i will run always")
#     if file1:
#         print("is file closed? ",file1.closed)
#         file1.close()
#         print("is file closed? ",file1.closed)


# print("i will run after reading file")
# print("i will run after reading file")
# list1=[]
# print(list1[2])
# print("i will run after reading file")
# print("i will run after reading file")



# file1=open("C:\\Users\\admin\\Desktop\\cleaner.bat","r")
# str1=file1.readline()
# print(str1)


file1=open("C:\\Users\\admin\\Desktop\\cleaner.bat","r")
str1=file1.readlines()
# print(str1)

for i in range(len(str1)):
    print(str1[i],end="")

file1.close()