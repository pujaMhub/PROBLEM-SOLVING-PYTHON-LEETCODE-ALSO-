def num(n):
    m=len(n)
    f={}
    for i in range(0,n):
        for j in range(i+1,n):
            if n[i]!=n[j]:
                f[n[i]]=0
    return f
n=[1,1,2,2,2,3,4,5,6]
print(num(n))