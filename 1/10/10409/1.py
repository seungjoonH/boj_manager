n,t=map(int,input().split())
l=[*map(int,input().split())]
print(len([*filter(lambda x:x<=t,[sum(l[:i+1])for i in range(n)])]))