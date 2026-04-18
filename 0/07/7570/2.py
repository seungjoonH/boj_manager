n,*a=map(int,open(0).read().split())
d=[0]*-~n
for c in a:d[c]=d[c-1]+1
print(n-max(d))