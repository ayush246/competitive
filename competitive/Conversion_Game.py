# https://www.hackerearth.com/practice/basic-programming/implementation/basics-of-implementation/practice-problems/algorithm/monk-and-conversion-game-code-monk/

t=int(input())
for i in range(0,t):
    N=int(input())
    l=[int(x) for x in input().split()]
    l2=[int(x) for x in input().split()]
    for y in range(0,N-1):
        l[y+1]+=-1*(l2[y]-l[y])
    if l[N-1]==l2[N-1]:
        print ("YES")
    else:
        print ("NO")