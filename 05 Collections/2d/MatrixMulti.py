r1=int(input("enter no. of rows of 1st matrix:"))
c1=int(input("enter no. of cols of 1st matrix:"))
r2=int(input("enter no. of rows of 2nd matrix:"))
c2=int(input("enter no. of cols of 2nd matrix:"))

if c1==r2:
    print("multiplication is possible ")
    matr1,matr2,matr3=[],[],[]
    #input
    print("enter the element in matrix 1:")
    for i in range(r1):
        matr1.append([])
        for j in range(c1):
            matr1[i].append(int(input()))

    print("enter the element in matrix 2:")
    for i in range(r2):
        matr2.append([])
        for j in range(c2):
            matr2[i].append(int(input()))

    #logic
    for i in range(r1):
        matr3.append([])
        for j in range(c2):
            matr3[i].append(0)
            for k in range(c1):
                matr3[i][j]+=matr1[i][k]*matr2[k][j]

    #print resultant
    print("the matrix is :")
    for i in range(r1):
        for j in range(c2):
            print(matr3[i][j],end="\t")
        print()
else:
    print("multiplication is not possible")