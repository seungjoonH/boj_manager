n, m = map(int, input().split())
l = [0] * n

for _ in range(m):
  a, b = map(int, input().split())
  l[a - 1] += 1; l[b - 1] += 1

print(*l, sep='\n')