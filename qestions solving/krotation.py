# k th position
# with slicing
num=[5,6,4,3,2,7,8]
k=int(input("enter integer:"))
n=len(num)
k= k % n # optimization part
num[:]=num[-k:]+num[:-k]
print(num)
