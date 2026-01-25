n=int(input());a,b,c,d,e,f=map(int,input().split())
m=sorted(map(min,[(a,f),(b,e),(c,d)]))
print(15*(n==1)or(n-2)*(5*n-6)*m[0]+4*(2*n-3)*sum(m[:2])+4*sum(m))