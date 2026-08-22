def sortornot(arr):
    n=len(arr)
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            return False
    return True
arr=[8,9,10,23]
print(sortornot(arr))