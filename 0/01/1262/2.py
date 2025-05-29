n, r1, c1, r2, c2 = map(int, input().split())
r = 2 * n - 1

for i in range(r1, r2 + 1):
  for j in range(c1, c2 + 1):
    x, y = i % r, j % r
    c = abs(x - n + 1) + abs(y - n + 1)
    c = chr(c % 26 + 97) if c < n else '.'
    print(c, end='')
  print()

# 154
'''
4 1 1 7 7
5 3 18 10 46
20000 0 19980 10 20010
20000 19980 19940 19990 19980
'''