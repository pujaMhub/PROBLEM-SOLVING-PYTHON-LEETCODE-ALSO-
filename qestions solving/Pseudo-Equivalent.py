# Pseudo-Equivalent Strings.
def Pseudo(w1,w2):
    count1=[0]*26
    count2=[0]*26

    for ch in w1:
        count1[ord(ch)-ord('a')]+=1
    for ch in w2:
        count2[ord(ch)-ord('a')]+=1

    for i in range(26):
        if abs[count1[i]-count2[i]] >3:
            return -1
    return min(w1,w2)