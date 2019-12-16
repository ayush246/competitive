# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/breakup-app/description/ 

N=int(input())
l=[]
for x in range(0,N):
    y=input().split()
    for x in y:
        if x.isdigit():
            if y[0]=='G:':
                l.append(x)
                l.append(x)
            elif y[0]=='M:':
                l.append(x)
d={}
for x in l:
    d[x]=0
for x in l:
    d[x]+=1
if ( max(d, key=d.get) == '19' ) or ( max(d, key=d.get) == '20' ):
    print ("Date")
else:
    print ("No Date")