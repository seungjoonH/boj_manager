import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

v, e = map(int, input().split())
edges = []
parents = dict((i + 1, i + 1) for i in range(v))

for i in range(e):
  edges.append((tuple(map(int, input().split()))))
edges.sort(key=lambda x: x[2])

def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  return parents[x]

def union(x, y):
  rx, ry = find(x), find(y)
  mn, mx = min(rx, ry), max(rx, ry)
  if rx != ry: parents[mx] = mn

def cycle(x, y): return find(x) == find(y)

result = 0

for (a, b, w) in edges:
  if cycle(a, b): continue
  union(a, b)
  result += w

print(result)