from sys import *
input = stdin.readline

setrecursionlimit(10 ** 6)

n = int(input())
graph = {i + 1: [] for i in range(n)}

while (ipt := input()):
  a, b = map(int, ipt.split())
  graph[a].append(b)
  graph[b].append(a)

dp = dict()

def search(node, parent):
  dp[node] = [0, 1]

  for next in graph[node]:
    if next == parent: continue
    
    search(next, node)
    
    dp[node][0] += dp[next][1]
    dp[node][1] += min(dp[next])

search(1, 0)

print(min(dp[1]))