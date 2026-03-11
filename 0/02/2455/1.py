m = c = 0
for _ in range(4):
  a, b = map(int, input().split())
  c += b - a
  m = max(m, c)

print(m)