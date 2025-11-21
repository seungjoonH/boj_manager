s = lambda x: (x > 0) - (x < 0)
g, p, t = map(int, input().split())
print('021'[s(g * p - (g + p * t))])