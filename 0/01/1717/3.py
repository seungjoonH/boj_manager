from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
parents = dict([(i, i) for i in range(n + 1)])

def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  return parents[x]

def union(x, y):
  rx, ry = find(x), find(y)
  mn, mx = min(rx, ry), max(rx, ry)
  if rx != ry: parents[mx] = mn

for _ in range(m):
  c, a, b = map(int, input().split())
  if c: print(['NO', 'YES'][find(a) == find(b)])
  else: union(a, b)