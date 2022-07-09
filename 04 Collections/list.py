#list is mutable and ordered collection of data(objects)

fruits=["Apple","strawberry",67,"mango",45.89,"Apple"]
basket=["Apple","strawberry","mango","Apple"]
numbers=[10,56,75,2,45,23]
# print(fruits)
# print(fruits[0])
# print("Apple" in fruits)
# print("mango" not in fruits)

# print(fruits.index("mango"))
# print(fruits.append("cherry"))
# print(fruits)
# print(fruits.count("Apple"))
# basket.sort()
# print(basket)
# numbers.sort()
# print(numbers)
print(fruits.pop())
fruits.pop()
print(fruits)

fruits.remove(67)
fruits.reverse()

fruits.extend(("banana","chiku"))
print(fruits)
fruits.insert(2,"papaya")
# fruits.clear()
fruits[2]="papaya 2.0"

print(fruits)