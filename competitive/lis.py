# https://www.hackerearth.com/practice/algorithms/searching/binary-search/practice-problems/algorithm/monk-meets-dynamic-array-code-monk/

def lis(arr): 
    n = len(arr) 
    lis = [1]*n 
    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n): 
        maximum = max(maximum , lis[i]) 
    return maximum 
    
a=[int(x) for x in input().split()]
l=[int(x) for x in input().split()]
for x in range (0,a[1]):
    l2=[int(x) for x in input().split()]
    if l2[0]==1:
        l.append(l2[1])
        print (lis(l))
    else:
        l.pop()
        print (lis(l))  
