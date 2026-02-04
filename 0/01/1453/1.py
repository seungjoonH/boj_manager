input();a=input().split();s=set(a)
print(sum(map(a.count,s))-len(s))