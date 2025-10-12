# regex in python 

# regex -> regular expression
# import re
# re -> regular expression module

Regex_Pattern = r'\b[tT]\w*'	# Do not delete 'r'.

import re

Test_String=''
with open('regex/data.txt', 'r') as file:
    Test_String = file.read()

# print(Test_String)
match = re.findall(Regex_Pattern, Test_String)
print(match)
print("Number of matches :", len(match))