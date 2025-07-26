from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
sets = dict([(i, set([i])) for i in range(n + 1)])
indices = dict([(i, i) for i in range(n + 1)])

def union(a, b):
  if a == b: return
  ai, bi = indices[a], indices[b]
  union_set = sets[ai].union(sets[bi])
  sets[ai] = sets[bi] = union_set
  for i in union_set: indices[i] = ai

for _ in range(m):
  c, a, b = map(int, input().split())
  if c: print(['NO', 'YES'][indices[a] == indices[b]])
  else: union(a, b)