_,*a=map(int,open(0))
for i in a:print('Bye'*((i+1)%(i%100)>0)or'Good')