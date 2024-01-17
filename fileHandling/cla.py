import sys

# print(sys.argv[0])
# print(sys.argv[0:])

with open(sys.argv[1],"r") as myfile:
    print(myfile.read())