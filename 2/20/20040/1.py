import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
parents = list(range(n))
sizes = [1] * n

def find(x):
  if parents[x] != x:
    parents[x] = find(parents[x])
  return parents[x]

def union(x, y):
  rx, ry = find(x), find(y)
  if rx == ry: return True

  mx, mn = max(rx, ry), min(rx, ry)
  parents[mn] = mx
  sizes[mx] += sizes[mn]
  return False

c = 0
for i in range(m):
  s, e = map(int, input().split())
  if union(s, e): c = i + 1; break
  
print(c)