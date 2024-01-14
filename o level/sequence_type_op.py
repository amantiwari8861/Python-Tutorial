numbers=[10,203,56,34,98,3,67]
# print(max(numbers))
# print(min(numbers))
# print(sum(numbers)//len(numbers))

max=numbers[0]
min=numbers[0]
total=0
for i in range(len(numbers)):
    if numbers[i]>max:
        max=numbers[i]
    if numbers[i]<min:
        min=numbers[i]
    total+=numbers[i]

print("max is ",max)
print("min is ",min)
print("mean is ",total//len(numbers))