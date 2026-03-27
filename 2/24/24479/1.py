from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10 ** 6)

n, m, r = map(int, input().split())

graph = { i + 1: [] for i in range(n) }
counts = { i + 1: 0 for i in range(n) }

for _ in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)

for key in graph: graph[key] = sorted(graph[key])

count = 1
visited = 1 << r - 1
counts[r] = 1

def dfs(node):
  global visited, count

  for adj in graph[node]:
    if visited & (1 << adj - 1): continue
    visited ^= 1 << adj - 1
    count += 1
    counts[adj] = count
    dfs(adj)

dfs(r)

print(*counts.values(), sep='\n')