_, *a = open(0)
d = lambda a, b: ((a + b - 1) * (a + b) ** 2) // 2
print(*[d(*map(int, r.split())) for r in a], sep='\n')