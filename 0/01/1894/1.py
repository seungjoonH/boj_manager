for a,b,c,d,e,f,g,h in map(lambda x:map(float,x.split()),open(0)):
 l=[(a,b),(c,d),(e,f),(g,h)];(a,b),(c,d),(e,f),(_,_)=sorted(l,key=l.count)
 print('%.3f %.3f'%(a+c-e,b+d-f))