import math
for _ in' '*int(input()):
 a,p1=map(int,input().split())
 r,p2=map(int,input().split())
 print(['Whole','Slice of'][a*p2>r*r*math.pi*p1],'pizza')