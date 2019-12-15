t=int(input())
for x in range (0,t):
    N=int(input())
    l=input()
    l=l.split()
    d={}
    for x in range(0,N):
        d[int(l[x])]=0
    for x in range(0,N):
        d[int(l[x])]+=1
    if d[min(d)] % 2 != 0:
        print ("Lucky")
    else:
        print ("Unlucky")
        