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
        if arr[i]>secondlarge and arr[i]!=largest: #already secondlargest considered
            secondlarge=arr[i]
    return secondlarge
arr=[7,5,14,6,22]
print(second(arr))

# method 4 with optimized
def secondlarge(arr):
    large=float("-inf")
    second=float("-inf")
    n=len(arr)
    for i in range(0,n):
        if arr[i]>large:# if arr[i] is big than arge second will update in large and large will update with value arr[i]
            second=large
            large=arr[i]
        elif arr[i]>second and arr[i]!=large:#if again second is big than arr[i] second variable will updated to arr[i] but
            # it must be not equal to the previous large number
            second=arr[i]
    return second
arr=[453,3,2,4,390]
print(secondlarge(arr))