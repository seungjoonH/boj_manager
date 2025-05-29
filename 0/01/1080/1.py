from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [int(input(), 2) for _ in range(n)]
b = [int(input(), 2) for _ in range(n)]
c = [a[i] ^ b[i] for i in range(n)]

count = 0
for i in range(n - 2):
  for j in range(m - 1, 1, -1):
    if c[i] & (1 << j):
      for k in range(3): c[i + k] ^= 7 << (j - 2)
      count += 1

print(-1 if sum(c) else count)