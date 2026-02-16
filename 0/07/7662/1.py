from heapq import *
from sys import stdin
input = stdin.readline

def test(n):
  l, r, visited = [], [], [False] * n

  for i in range(n):
    type, value = input().split()
    v = int(value)
    
    if type == 'I':
      heappush(l, (v, i))
      heappush(r, (-v, i))
      visited[i] = True
      continue

    if v == 1:
      while r and not visited[r[0][1]]: heappop(r)
      if r: visited[r[0][1]] = False; heappop(r)
  
    elif v == -1:
      while l and not visited[l[0][1]]: heappop(l)
      if l: visited[l[0][1]] = False; heappop(l)

  while l and not visited[l[0][1]]: heappop(l)
  while r and not visited[r[0][1]]: heappop(r)

  if not l: print('EMPTY')
  else: print(-r[0][0], l[0][0])

  
for _ in range(int(input())): test(int(input()))
