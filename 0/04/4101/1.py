while'0 0'!=(i:=input()):print(["No","Yes"][eval(i.replace(' ','>'))])
while(i:=input())!='0 0':a,b=i.split();print(["No","Yes"][a>b])
while(i:=input())!='0 0':a,b=map(int,i.split());print(["No","Yes"][a>b])