s = input(); n = len(s)
r, c = max((i, n // i) for i in range(1, int(n ** .5) + 1) if n / i == n // i)
print(*[s[r * i + j] for j in range(r) for i in range(c)], sep="")