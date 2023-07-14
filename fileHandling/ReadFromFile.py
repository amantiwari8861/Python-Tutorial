# file1=open("C:\\Users\\Aman_Tiwari\\Desktop\\aist.txt","r")
# str1=file1.read()
# print(str1)

# try:
#     file1=open("C:\\Users\\Aman_Tiwari\\Desktop\\applist.txt","r")
#     # file1=open("C:\\Users\\Aman_Tiwari\\Desktop\\sitara.bmp","rb")
#     str1=file1.read()
#     print("The Content in File is :\n",str1)
# except FileNotFoundError:
#     print("File doesn't exist!!")
# except:
#     print("unable to open file may be u don't have permissions to open file\n or file is corrupted")


# file1=open("C:/Users/Aman_Tiwari/Desktop/applist.txt","r")
# str1=file1.readline()
# print(str1)


file1=open("C:/Users/Aman_Tiwari/Desktop/applist.txt","r")
str1=file1.readlines()
# print(str1)


# for i in range(len(str1)):
#     print(str1[i],end="")


file1.close()