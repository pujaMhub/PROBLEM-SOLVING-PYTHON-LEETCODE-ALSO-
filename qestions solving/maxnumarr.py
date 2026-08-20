# method 1 
def large(arr):
    largest=arr[0]
    n=len(arr)
    for i in range(0,n):
        largestt=max(largest,arr[i])
    return largest
arr=[6,5,4,4,1]
print(large(arr))

# method 2
def large(arr):
    largest=arr[0]
    n=len(arr)
    for i in range(0,n):
        if arr[i]>largest:
            largest=arr[i] # only i print the index
    return largest
arr=[5,6,4,7]
print(large(arr))

# method 3
def large(arr):
    largest=float("-inf")
    n=len(arr)
    for i in range(0,n):
        largest=max(largest,arr[i])
    return largest
arr=[6,5,4,4,1]
print(large(arr))