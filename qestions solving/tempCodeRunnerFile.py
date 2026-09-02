def dup(arr):
    n=len(arr)
    freq_map={}
    for i in range(0,n):
        freq_map[arr[i]]=0
    j=0
    for k in freq_map:
        arr[j]=k
        j+=1
    return j
arr=[1,2,3,3,4,5,7,7,8,10]
print(dup(arr))