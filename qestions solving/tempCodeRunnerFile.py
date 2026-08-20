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
arr=[7,5,4,6,22]
print(second(arr))