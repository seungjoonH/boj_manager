r=lambda x:int(str(x)[::-1])
print(r(sum(map(r,input().split()))))