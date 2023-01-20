# Q.1 take marks from user and find percentage 

total=0
marks=[]
sub=int(input("Enter subjects \n"))
for i in range(sub):
    marks.append(float(input("enter ur marks :")))
    total=total+marks[i]

print(marks)
print("total is ",total)
print("PERCENTAGE is ",total/sub," %")

'''   
    let sub=5,marks=[],total=0

    step 1: i=0,marks=[],total=0
            marks.append(68)  => marks=[68]
            total=total+marks[0]
            total=0+68  =>68

    step 2: i=1,marks=[68],total=68
            marks.append(23) => marks=[68,23]
            total=total+marks[1]
            total=68+23 => 91

    step 3: i=2,marks=[68,23],total=91
            marks.append(12) => marks=[68,23,12]
            total=total+marks[2]
            total=91+12 => 103

            
    step 4: i=3,marks=[68,23,12],total=103
            marks.append(8) => marks=[68,23,12,8]
            total=total+marks[3]
            total=103+8 => 111
            
    step 5: i=4,marks=[68,23,12,8],total=111
            marks.append(15) => marks=[68,23,12,15]
            total=total+marks[4]
            total=111+15 => 126

    step 6: i=5 , 5 < 5 false loop terminated







