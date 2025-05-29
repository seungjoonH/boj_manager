from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
x, y = map(int, input().split())

graph = {}
for _ in range(int(input())):
  a, b = map(int, input().split())
  if a not in graph: graph[a] = []
  if b not in graph: graph[b] = []
  
  graph[a].append(b)
  graph[b].append(a)

def search(node, find):
  dq = deque([node])
  levels, visited = {}, []

  level = 0
  while dq:
    node = dq.popleft()
    if node in levels: level = levels[node]

    if node in visited: continue
    visited.append(node)

    for child in graph[node]: 
      if child in visited: continue
      dq.append(child)
      levels[child] = level + 1

  return -(find not in levels) or levels[find]

print(search(x, y))