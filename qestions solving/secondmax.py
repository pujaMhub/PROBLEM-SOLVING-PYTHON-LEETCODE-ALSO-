# method 1
arr=[56,74,3,5,2,3]
arr.sort()
print(arr[-2])

# method 2
def second(arr):
    arr.sort()
    n=len(arr)
    return arr[n-2]
arr=[7,5,4,6,22]
print(second(arr))

# method 3 bettter
def second(arr):
    largest=float("-inf")
    secondlarge=float("-inf")
    n=len(arr)
    for i in range(0,n):
        largest=max(largest,arr[i])
    for i in range(0,n):
        if arr[i]>secondlarge and arr[i]!=largest: #already secondlargest dhorai ache
            secondlarge=arr[i]
    return secondlarge
arr=[7,5,14,6,22]
print(second(arr))