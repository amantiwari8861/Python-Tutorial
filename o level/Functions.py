# numbers = [5, 8, 2, 10, 3, 8, 15, 5, 10, 8]

# # Counting frequency using a dictionary
# frequency_dict = {}

# # print(55 in [10,30,550,67])
# # frequency_dict[99]=3
# # print(frequency_dict)

# for num in numbers:
#     if num in frequency_dict:
#         frequency_dict[num] += 1
#     else:
#         frequency_dict[num] = 1

# # print(frequency_dict)
# # Print frequency dictionary
# print("Frequency of elements:")
# for key,value in frequency_dict.items():
#     # print(key,":",value)
#     print(f"{key}: {value}")


# a,b,c=10,20,0
# c=a+b
# print("the sum of",a,"and",b,"is",c)
# print(f"the sum of {a} and {b} is {c}.")

import random
import math
from datetime import datetime

# String functions
sample_string = "Hello, World!"
# print("String Functions:")
# print(f"Original String: {sample_string}")  # Hello, World!
# print(f"Count of 'l': {sample_string.count('l')}")  # Count of 'l': 3
# print(f"Find 'World': {sample_string.find('World')}")  # Find 'World': 7
# print(f"Capitalize: {sample_string.capitalize()}")  # Capitalize: Hello, world!
# print(f"Title Case: {sample_string.title()}")  # Title Case: Hello, World!
# print(f"Lowercase: {sample_string.lower()}")  # Lowercase: hello, world!
# print(f"Uppercase: {sample_string.upper()}")  # Uppercase: HELLO, WORLD!
# print(f"Swapcase: {sample_string.swapcase()}")  # Swapcase: hELLO, wORLD!
# print(f"Is Lowercase? {sample_string.islower()}")  # Is Lowercase? False
# print(f"Is Uppercase? {sample_string.isupper()}")  # Is Uppercase? False
# print(f"Is Title Case? {sample_string.istitle()}")  # Is Title Case? True
# print(f"Replace 'Hello' with 'Hi': {sample_string.replace('Hello', 'Hi')}")  # Replace 'Hello' with 'Hi': Hi, World!

# sample_string="       Hello World! 2.0         "
# print("length is :",len(sample_string))
# print("after stripping length is ",len(sample_string.strip()))
# print("after stripping length is ",len(sample_string.strip()))
# print("after left stripping length is ",len(sample_string.lstrip()))
# print("after right stripping length is ",len(sample_string.rstrip()))

# sample_string="the quick brown fox jumps over the lazy dog."

# print(sample_string.split(' '))
# words=sample_string.split(' ')
# print(str.join("-",words))
# print(sample_string.partition(" "))

# print(f"Partition: {sample_string.partition(', ')}")  # Partition: ('Hello', ', ', 'World!')
# print(f"Is Space? {sample_string.isspace()}")  # Is Space? False
# print(f"Is Alpha? {sample_string.isalpha()}")  # Is Alpha? False
# print(f"Is Digit? {sample_string.isdigit()}")  # Is Digit? False
# print(f"Is Alphanumeric? {sample_string.isalnum()}")  # Is Alphanumeric? False
# print(f"Starts with 'Hello'? {sample_string.startswith('Hello')}")  # Starts with 'Hello'? True
# print(f"Ends with 'World!'? {sample_string.endswith('World!')}")  # Ends with 'World!'? True

# print(f"Encoded: {sample_string.encode()}")  # Encoded: b'Hello, World!'
# print(f"Decoded: {sample_string.encode().decode()}")  # Decoded: Hello, World!

# # Numeric functions
# numbers_list = [3, 7, 1, 9, 4, 6]
# print("\nNumeric Functions:")
# print(f"Evaluation: {eval('2 + 3 * 4')}")  # Evaluation: 14
# print(f"Maximum: {max(numbers_list)}")  # Maximum: 9
# print(f"Minimum: {min(numbers_list)}")  # Minimum: 1
# print(f"Power of 2^3: {pow(2, 3)}")  # Power of 2^3: 8
# print(f"Rounded value: {round(4.567)}")  # Rounded value: 5
# print(f"Integer part: {int(4.567)}")  # Integer part: 4
# print(f"Random number between 1 and 10: {random.randint(1, 10)}")  # Random number between 1 and 10: ...
# print(f"Ceiling of 4.3: {math.ceil(4.3)}")  # Ceiling of 4.3: 5
# print(f"Floor of 4.7: {math.floor(4.7)}")  # Floor of 4.7: 4
# print(f"Square Root of 16: {math.sqrt(16)}")  # Square Root of 16: 4.0

# # Date & Time Functions
current_datetime = datetime.now()
print("\nDate & Time Functions:")
print(f"Current Date & Time: {current_datetime}")  # Current Date & Time: ...
print(f"Year: {current_datetime.year}")  # Year: ...
print(f"Month: {current_datetime.month}")  # Month: ...
print(f"Day: {current_datetime.day}")  # Day: ...
print(f"Hour: {current_datetime.hour}")  # Hour: ...
print(f"Minute: {current_datetime.minute}")  # Minute: ...
print(f"Second: {current_datetime.second}")  # Second: ...
print(f"Microsecond: {current_datetime.microsecond}")  # Microsecond: ...
