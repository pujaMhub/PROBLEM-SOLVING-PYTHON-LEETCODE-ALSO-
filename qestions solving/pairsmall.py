#smallest  pair of an arr
def pair(arr):
    n=len(arr)

    small=float('inf')
    si=sj=0
    for i in range(n):
        for j in range(i+1,n):
            total=arr[i]+arr[j]

            if total<small:
                small=total
                si=i
                sj=j
    return small,si,sj
arr=[2,1,5,6,7]
print(pair(arr))
 
