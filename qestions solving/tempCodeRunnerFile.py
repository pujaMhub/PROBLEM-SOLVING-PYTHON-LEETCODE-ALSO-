def string(s):
    count=0
    result=[]
    prev=""

    for ch in s:
        if ch in prev:
            count+=1
        else:
            count=1
            prev=ch
        if count<=2:
            result.append(ch)
    return "".join(result)
s=input("enter")
print(string(s))