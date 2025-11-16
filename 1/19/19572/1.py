d1, d2, d3 = map(int, input().split())
c = (d2 + d3 - d1) / 2
a = d2 - c; b = d1 - a
t = a, b, c
if any(map(lambda x: x <= 0, t)): print(-1)
else: print(1); print(*t)
