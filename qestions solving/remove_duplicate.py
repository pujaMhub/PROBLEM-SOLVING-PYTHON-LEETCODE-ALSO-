# remove duplicate from array values and count also
def dup(arr):
    r=[]
    c=0
    for i in arr:
        if i not in r:
            r.append(i)
            c+=1
    r.sort()
    return r,c
arr=[1,44,44,2,1,2]
print(dup(arr))
