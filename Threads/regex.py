"""
Special Characters in Regex
.: Matches any character except a newline.
^: Matches the start of the string.
$: Matches the end of the string.
*: Matches 0 or more repetitions of the preceding pattern.
+: Matches 1 or more repetitions of the preceding pattern.
?: Matches 0 or 1 repetition of the preceding pattern.
[]: Matches any one of the characters inside the brackets.
\d: Matches any digit (equivalent to [0-9]).
\w: Matches any alphanumeric character (equivalent to [a-zA-Z0-9_]).
\s: Matches any whitespace character.
\b: Matches a word boundary.
"""
import re

# match = re.search(r'[\s]{0,}', 'string to search')
# if match:
#     print("Found:",match.group(),".")

# match = re.match(r'[a-z]{0,}', 'string to search')
# if match:
#     print("Found:", match.group())

matches = re.findall(r'[a-z]', 'strING to search')
print("All matches:", matches)

# matches = re.finditer(r'[a-z\s]', 'string to search')
# for match in matches:
#     print("Found:", match.group())

# result = re.sub(r'[a-z\s]', 'replacement', 'string to search')
# print("Modified string:", result)


# Example string
# text = "My phone number is 123-456-7890."

# # Search for a phone number pattern
# match = re.search(r'\d{3}-\d{3}-\d{4}', text)
# if match:
#     print("Phone number found:", match.group())




# def divide(a, b):
#     assert b != 0, "The denominator must not be zero"
#     return a / b

# result = divide(10, 0)  # This will raise an AssertionError
