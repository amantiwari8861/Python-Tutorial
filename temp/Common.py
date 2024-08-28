# from collections import Counter

# def iterate_elements(lst):
#     result = []
#     counts = Counter(lst)
#     for elem, count in counts.items():
#         result.extend([elem] * count)
#     return result

# sample_list = ['p', 'p', 'p', 'p', 'q', 'q']
# print(iterate_elements(sample_list))



# from collections import Counter

# def most_common_elements(s):
#     return Counter(s).most_common(3)

# sample_string = 'lkseropewdssafsdfafkpwe'
# print(most_common_elements(sample_string))


def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

greet(name="Alice", age=30, city="New York")

my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for key in sorted(my_dict, reverse=True):
    print(f"{key}: {my_dict[key]}")
