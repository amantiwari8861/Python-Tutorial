# try:
#     with open("C:\\Users\\admin\\Desktop\\cleaner.bat","r") as myfile:
#         print(myfile.tell())
#         print(myfile.readline())
#         print(myfile.tell())
#         print(myfile.readline())
#         print(myfile.tell())
# except FileNotFoundError:
#     print("file doesn't exist!!")

try:
    with open("fileHandling/MyData.txt","rb+") as myfile:
        print(myfile.tell())
        print(myfile.read(5).decode())
        print(myfile.tell())
        # myfile.seek(-5,1)
        # print("setting file cursor at starting:",myfile.tell())
        myfile.write("hello".encode("utf-8"))
        print(myfile.readline().decode())
        # print(myfile.readline().strip())
        print(myfile.tell())
except FileNotFoundError:
    print("file doesn't exist!!")
