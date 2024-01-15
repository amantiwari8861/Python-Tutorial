age=int(input("enter ur age:"))

if age<18:
    print("not eligible for vote!")
    raise RuntimeError("u r not eligible byee!")
else:
    print("eligible for vote!")

print("any other codes ")