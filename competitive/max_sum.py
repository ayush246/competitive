# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/maximum-sum-4-f8d12458/description/

N=int(input())
l=[int(x) for x in input().split()]
le=1
st=0
l.sort(reverse=True)
su=l[0]
for x in l:
    st+=x
    if st>su:
        su+=x
        le+=1
print (su,le)