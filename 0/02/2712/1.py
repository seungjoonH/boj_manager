d={'kg':[2.2046,'lb'],'lb':[0.4536,'kg'],'l':[0.2642,'g'],'g':[3.7854,'l']}
_,*a=map(str.split,open(0))
for(n,u)in a:print('%.4f %s'%(d[u][0]*float(n),d[u][1]))