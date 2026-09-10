# 196
# Output:
# 96245
# Explanation:
# I
# The digits 1 and 0 of array arr are replaced by the digits 9 and 6 of array rep 
# to maximize the number represented by arr.
# Sample input
# 64
# 307823
# 6199
# Sample Output
# 997863
def reparr(arr,rep):
    rep.sort(reversed=True)

    for i in range(len(arr)):
        for j in range(len(rep)):
            if rep[j]>arr[i]:
                arr[i]=rep[j]
                rep.pop(j) #use to 6,7,9,9=6,7,9 pop  the first 9
                break
    return arr
