#smallest  pair of an arr
def pair(arr):
    n=len(arr)

    small=float('inf')
    for i in range(n):
        for j in range(i+1,n):
            total=arr[i]+arr[j]

            if total<small:
                small=total
    return small
arr=[2,1,5,6,7]
print(pair(arr))
 
