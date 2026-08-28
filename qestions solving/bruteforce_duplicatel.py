def removeDuplicates(nums):
    n=len(nums)
    freq_map={}
    for i in range(0,n):
        freq_map[nums[i]]=0
    j=0
    for k in freq_map:
        nums[j]=k
        j+=1
    return j
arr=[1,2,3,3,4,5,7,7,8,10]
print(removeDuplicates(arr))