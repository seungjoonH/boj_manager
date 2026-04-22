n, k = map(int, open(0))
q = k + 60
print(n * 1500 if n <= q else q * 1500 + (n - q) * 3000)