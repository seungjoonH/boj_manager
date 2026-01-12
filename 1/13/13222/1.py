n,w,h=map(int,input().split())
for _ in' '*n:print(['YES','NO'][int(input())>(w**2+h**2)**.5])