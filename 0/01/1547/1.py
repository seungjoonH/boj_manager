n = 1
for _ in range(int(input())):
  l = list(map(int, input().split()))
  if n not in l: continue
  n = l[1 - l.index(n)]
print(n)