n,*a=[*map(str.split,open(0))];z=[*zip(*a)]
print(*[sum((int(v)*(z[i].count(v)==1))for i,v in enumerate(e))for e in a],sep='\n')