import re
input()
y = lambda x: (1 + x // 30) * 10
m = lambda x: (1 + x // 60) * 15
t = list(map(int, input().split()))
ys, ms = sum(map(y, t)), sum(map(m, t))
res = f"{'Y '[ys > ms]} {'M '[ys < ms]} {min(ys, ms)}"
print(re.sub(r'\s+', ' ', res.strip()))