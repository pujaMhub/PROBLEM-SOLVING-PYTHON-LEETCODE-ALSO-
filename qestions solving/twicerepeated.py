# Example:

# Input:

# abbbccdeab

# Output:

# abbccdeab

# Explanation:

# Since the input string is having the character 'b' thrice, we require 
# the characters in the string doesn't repeat themselves more than twice,
#  so we omit 'b' and desired string would be "abbccdeab".

def string(s):
    result=[] # ofc need to take and compare length of result 

    for ch in s:
        if len(result)<2 or not(result[-1]==ch and result[-2]==ch):
            result.append(ch)
    r="".join(result)
    return r
s=input()
print(string(s))