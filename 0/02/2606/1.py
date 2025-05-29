from sys import stdin
input = stdin.readline

com = int(input())
graph = [[] for _ in range(com)]
check = [0 for _ in range(com)]

for _ in range(int(input())):
  a, b = map(int, input().split())
  graph[a - 1].append(b - 1)
  graph[b - 1].append(a - 1)
  
def dfs(p):
  if check[p]: return
  check[p] = 1
  for e in graph[p]: dfs(e)
    
dfs(0)
print(sum(check) - 1)