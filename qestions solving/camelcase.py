def camelcase(s):
    word=""
    for ch in s:
        if s.isupper():
            print(word.swapcase())
            word =ch
        else:
            word+=ch
    print(word.swapcase())
s=input()
camelcase(s)
