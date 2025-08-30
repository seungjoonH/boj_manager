def p(x):l,o,v,e=map(x.count,"LOVE");return(l+o)*(l+v)*(l+e)*(o+v)*(o+e)*(v+e)
n,_,*s=map(str.strip,open(0));print(min(s,key=lambda t:(-p(t+n)%100,t)))