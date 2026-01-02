a,b=map(int,open(0))
print(a,b,*[a*int(i)for i in str(b)[::-1]],a*b,sep='\n')