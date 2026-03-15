from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
ipts = [[[int(i == 'H') for i in input().split()] for _ in range(3)] for _ in range(n)]

def to_index(mat): return ''.join(''.join(map(str, row)) for row in mat)
indices = [int(to_index(ipt), 2) for ipt in ipts]
dp = [-1] * (1 << 9)
dp[0] = dp[-1] = 0

r1 = lambda x: x ^ int('111000000', 2)
r2 = lambda x: x ^ int('000111000', 2)
r3 = lambda x: x ^ int('000000111', 2)
c1 = lambda x: x ^ int('100100100', 2)
c2 = lambda x: x ^ int('010010010', 2)
c3 = lambda x: x ^ int('001001001', 2)
x1 = lambda x: x ^ int('100010001', 2)
x2 = lambda x: x ^ int('001010100', 2)
funcs = [r1, r2, r3, c1, c2, c3, x1, x2]

dq = deque([0, (1 << 9) - 1])

while dq:
  curr = dq.popleft()
  count = dp[curr]
  for func in funcs:
    next = func(curr)
    if dp[next] >= 0: continue
    dp[next] = count + 1
    dq.append(next)

for index in indices: print(dp[index])