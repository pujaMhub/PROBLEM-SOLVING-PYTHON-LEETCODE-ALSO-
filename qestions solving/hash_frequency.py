def freq(arr):
    freq_arr={}
    for i in arr:
        freq_arr[i]=freq_arr.get(i,0)+1
    return freq_arr
arr=[1,1,3,2,4,3,3,4,4]
print(freq(arr))