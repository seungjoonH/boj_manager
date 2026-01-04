l=[sum(map(int,p))for p in map(str.split,open(0))]
m=max(l);p=1+l.index(m);print(p,m)