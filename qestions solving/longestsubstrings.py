# input like 'ggmmmggggmmmm' which m consecutive is longest m = 4
def longest(s):
    c=0
    maxcount=0
    for ch in s:
        if ch=='g':
            c+=1
            maxcount=max(maxcount,c)
        else:
            c=0
    return maxcount
s='gmmmmgggggmmmmmmm'
print(longest(s))