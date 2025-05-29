w,x,y,z=map(int,input().split())
def g(i,j):m=max(abs(i),abs(j));return(2*m+i+j)*(1-2*(i<j))+1+4*m*m
for i in range(w,y+1):print(*[f'%{len(str(max(g(w,x),g(y,x),g(y,z))))}d'%g(i,j)for j in range(x,z+1)])