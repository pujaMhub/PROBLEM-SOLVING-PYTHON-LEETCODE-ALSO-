def longsub(s):
    result =""

    for ch in s:
        if ch not in result:
            result+=ch
        else:
            result=result[result.index(ch)+1:]
            result +=ch
    return result
s = input()
print(longsub(s))