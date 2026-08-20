
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