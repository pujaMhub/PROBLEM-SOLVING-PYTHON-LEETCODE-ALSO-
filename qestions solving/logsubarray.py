# 01. Longest Mirror Sub-array

# Problem Statement

# You are given a binary array arr of size N and you need to find and print the length of the longest sub-array which satisfies the following

# conditions:

# The sub-array must consist of an equal number of Os and 1s.

# The sub-array must contain only one distinct element (0 or 1) in each half. For example: [0, 0, 1, 1] and [1, 0] are valid while [0, 1, 0, 1] and [1, 0, 0, 1] are not.

# Note:

# A sub-array is a slice from the array which is contiguous (i.e. the elements occupy consecutive positions) and inherently maintains the order of elements. For example, the sub-arrays of the array {1, 2, 3} are {1}, {1, 2}, {1, 2, 3}, {2}, {2, 3}, and {3}.

# Page 10 of 22

# 1572 words

# English (India)

# Accessibility: Good to go

# Input Format:

# The input is in the following format:

# The first line contains an integer, i.e. N.

# Each of the next N lines has a single element denoting the elements of the array arr.

# Input will be read from the STDIN by the candidate

# Output Format:

# Print the length of the longest sub-array which satisfies the given conditions.

# The output will be matched to the candidate's output printed on the STDOUT

# Constraints:

# 1SNS10

# 0s arr[i] ≤ 1

def sub(arr,n):
    ans=0

    for i in range(n):
        c0=0
        c1=0
        for j in range(i,n):
            if arr[j]==0:
                c0+=1
            else:
                c1+=1
            if c0==c1:
                ans=max(ans,c0+c1)
    return ans
n=int(input("enter:"))
arr=[int(input()) for _ in range(n)]
print(sub(arr,n))


    