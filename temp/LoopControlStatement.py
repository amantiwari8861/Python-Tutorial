numbers=[10,20,30,40,78,346,238,40,99,78,346,238,40,78,346,238]
# #linear search
# key=int(input("enter no. to be searched:"))
# for i in range(len(numbers)):
#     if key==numbers[i]:
#         print(numbers[i],"found at postion",i,"in list.")
#         break

for num in numbers:
    if num==40:
        continue
    print("the element is",num)

