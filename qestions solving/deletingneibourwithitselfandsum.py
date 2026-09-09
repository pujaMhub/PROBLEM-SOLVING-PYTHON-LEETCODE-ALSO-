# Every round:

# Find the smallest number currently remaining.
# If there are multiple smallest numbers, choose the one with the smallest/leftmost index.
# Add that minimum number to total.
# Delete:
# the minimum itself
# its immediate left neighbor, if it exists
# its immediate right neighbor, if it exists
# Repeat until the array becomes empty.

# That's it.
def deleting(arr):
    total =0

    while arr:
        mini=min(arr)

        i=arr.index(mini)
        total+=mini

        if i+1<len(arr):
            del arr[i+1]
        del arr[i]
        if i-1>=0:
            del arr[i-1]
    return total
n=int(input())
arr = []

for _ in range(n):
    arr.append(int(input()))

print(deleting(arr))