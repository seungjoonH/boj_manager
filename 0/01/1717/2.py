from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
indices = dict([(i, i) for i in range(n + 1)])

def union(a, b):
  if a == b: return
  ai, bi = indices[a], indices[b]
  for i, v in indices.items(): 
    if v == bi: indices[i] = ai

for _ in range(m):
  c, a, b = map(int, input().split())
  if c: print(['NO', 'YES'][indices[a] == indices[b]])
  else: union(a, b)