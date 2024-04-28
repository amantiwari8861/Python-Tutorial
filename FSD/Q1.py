def solve(S1, S2):
    L1 = len(S1)
    L2 = len(S2)
    S = ['A'] * (L1 + L2 - 1)

    for ind in range(L2):
        if S2[ind] == 'T':
            for ind2 in range(L1):
                if S[ind + ind2] != S1[ind2]:
                    return -1
        else:
            for ind2 in range(L1):
                if S[ind + ind2] == 'A':
                    S[ind + ind2] = S1[ind2]

    return ''.join(S)

# Example Usage
S1 = "ABCA"
S2 = "TFFF"
result = solve(S1,S2)
print(result)

# Given a string S1 of length L1 Consisting of Latin uppercase alphabets only and a string S2 of length L2 consisting of haracters T and F only Generate a lexicographically smalIest string S of length (L1 + L2 - 1) such that a substring of length L1 in string starting at index i (0 <= i < L2) is equal to S1 if and only if ith element of S2 is T else not. If no such string can be generated, print -1 Notes: A string a is lexicographically smaller than a string b if and only if one of the following holds: • a is a prefix of b, but a !=b; • in the first position where a and b differ, the string a has a letter that appears earlier in the alphabet then the corresponding letter in b. Find the lexicographically smallest string S which satisfies the given condition. Complete the solve function. This function takes the following 2 parameters and returns the answer. S1 Represents a string S1 S2 Represents a string S2 Input format for custom testing Note: Use this input format if you are testing against custom input or writing code The first line contains T, which represents the number of test cases. For each test case: The first line contains a string S1 The second line contains a string S2 Output format For each test case, print a string S in a new line or -1 if not possible.