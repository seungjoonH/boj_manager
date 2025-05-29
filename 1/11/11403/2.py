from collections import deque
from sys import stdin
input = stdin.readline

n = int(input())
graph = [[*map(int, input().split())] for i in range(n)]
check = [[0] * n for i in range(n)]

def search(root):
  visited = deque([-1])

  def _search(node):
    if root == visited[-1]: 
      visited.pop(); return

    for child in range(n):
      if graph[node][child]:
        if child in visited: continue
        visited.append(child)
        check[root][child] = 1
        _search(child)
  
  _search(root)

for i in range(n): search(i)
for i in check: print(*i)