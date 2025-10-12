
# file2=open("C:\\Users\\admin\\Desktop\\aman.txt","w")
# file2.write(input("enter data in file:"))
# print("written in file succesfully!")
# file2.close()

file2=open("C:\\Users\\admin\\Desktop\\aman.txt","a")
file2.write("\n"+input("enter data in file:"))
print("appended in file!")
file2.close()