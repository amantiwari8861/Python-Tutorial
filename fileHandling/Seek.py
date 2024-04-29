# import os
# print(os.getcwd())
try:
    with open("fileHandling\\Hello.txt","r") as myfile:
        print(myfile.tell())
        print(myfile.readline())
        print(myfile.tell())
        myfile.seek(0)
        print(myfile.tell())
        print(myfile.readline())
except FileNotFoundError:
    print("file doesn't exist!!")
