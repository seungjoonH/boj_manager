from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n)]
dq = deque()

visited = 0
def init(): global dq, visited; dq = deque(); visited = 0
def toggle(node): global visited; visited ^= 1 << node
def add(node): dq.append(node); toggle(node)
def pop(): toggle(dq.pop())
def has(node): return visited & (1 << node)

for _ in range(m): 
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

res = 0

def dfs(root):
  init()
  add(root)
  _dfs(root)

def _dfs(node):
  global res
  if res: return res

  for adj in graph[node]:
    if has(adj): continue
    add(adj)
    if len(dq) == 5: res = 1; break
    _dfs(adj)
    pop()

for i in range(n): dfs(i)
print(res)