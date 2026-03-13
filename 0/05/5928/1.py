d, h, m = map(int, input().split())
s = 11 * 1440 + 11 * 60 + 11
e = d * 1440 + h * 60 + m
res = e - s
print(res if res >= 0 else -1)