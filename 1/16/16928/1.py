from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())

routes = dict([map(int, input().split()) for _ in range(n + m)])
board = dict()

for i in range(1, 100):
  board[i] = {(j in routes) and routes[j] or j for j in range(i + 1, min(i + 7, 101))}

dq = deque([(1, 0)])
mn = float('inf')

while dq: 
  curr, count = dq.popleft()
  if curr == 100: mn = count; break 

  for next in board[curr]:
    el = (next, count + 1)
    if el in dq: continue
    dq.append(el)

print(mn)
