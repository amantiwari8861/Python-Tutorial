import shapesLib
import os

while True:
    os.system("cls")
    print("\t\t1.square")
    print("\t\t2.rectangle")
    print("\t\t3.cylinder")
    print("\t\t4.cone")
    print("\t\t5.exit")

    choice1=int(input("\n\t\tchoose shape :"))

    if choice1==1:
        print("\t\t1.area")
        print("\t\t2.perimeter")

        choice=int(input("\t\tenter ur choice :"))
        if choice==1:
            side=float(input("enter side :"))
            result=shapesLib.areaOfSquare(side)
            print("the area of square having side",side,"is",result)
        elif choice==2:
            side=float(input("enter side :"))
            result=shapesLib.perimeterOfSquare(side)
            print("the perimeter of square having side",side,"is",result)

    elif choice1==2:
        print("\t\t1.area")
        print("\t\t2.perimeter")

        choice=int(input("\t\tenter ur choice :"))
        if choice==1:
            length=float(input("enter length :"))
            breadth=float(input("enter breadth :"))
            result=shapesLib.areaOfReactangle(length,breadth)
            print("the area of rectangle is:",result)
        elif choice==2:
            length=float(input("enter length :"))
            breadth=float(input("enter breadth :"))
            result=shapesLib.perimeterOfReactangle(length,breadth)
            print("the perimeter of rectangle is:",result)


    elif choice1==5:
        break
    input("Press enter to continue.......")