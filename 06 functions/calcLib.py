def add(nums):
    sum=0
    for i in range(len(nums)):
        sum+=nums[i]
    return sum

def multi(nums):
    sum=nums[0]
    for i in range(len(nums)-1):
        sum*=nums[i+1]
    return sum

def div(nums):
    sum=0
    for i in range(len(nums)):
        sum/=nums[i]
    return sum

def sub(nums):
    sum=0
    for i in range(len(nums)):
        sum-=nums[i]
    return sum