from collections import deque

# data=deque([20,40,50,90])
data=deque()
data.append(10)
data.append(20)
data.append(10)
data.append(30)
# print(data)

data.appendleft(5)
data.appendleft(2)

# print(data)

# data.pop()
# print(data)

# data.popleft()
# print(data)

# data.pop(10) #error
# print(data)

# data.remove(20)
# print(data)

# print(data.index(10))

# print(data[0])
# print(data[1])
# print(data[-1])

# print(data.count(10))
data.extend([40,50,60])
data.extendleft([-1,-2,0,1])

print(data)
# data.rotate(4)
# data.rotate(-4)
data.insert(5,3.5)
print(data)
