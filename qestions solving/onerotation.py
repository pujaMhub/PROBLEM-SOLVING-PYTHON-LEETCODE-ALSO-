# rotated an array byt one [5,6,7,8,4,3]=[3,5,6,7,8,4]-- 1 step ahead and 3 goes at it first cause of shift
# with slice
num=[5,6,7,8,4,3]
k=int(input("enter one:"))
num[:]=num[-k:]+num[:-k] # we are not creating another array we change the existing thats why i use num[:] varaible list to store
print(num) #[3, 5, 6, 7, 8, 4]output

# without slicing
def rotation(arr):
    n=len(arr)
    temp = arr[n-1]
    for i in range(n-2,-1,-1):
        arr[i+1]=arr[i]
    arr[0]=temp
    return arr
arr=[5,6,7,4,2] # n-2 theke -1 kore -1 obdhi kore jabe, cause n-2=i=4,sei i ta store hbe i+1=2 r jaygay
# ei kre kre swap hbe, then 2 ta which is temp=arr[n-1]=2 store hbe arr[0] index e
print(rotation(arr))
