n, *a = map(int, open(0))
print(sum(abs(i - j) for i, j in zip(sorted(a), range(1, n + 1))))