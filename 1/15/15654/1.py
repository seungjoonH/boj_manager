# from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
numbers = sorted(map(int, input().split()))

def permutations(numbers, r):
  result = []

  def dfs(path, used):
    print(path, [int(i) for i in used])
    if len(path) == r: result.append(path[:]); return
    for i in range(n):
      if used[i]: continue
      used[i] = True
      dfs(path + [numbers[i]], used)
      used[i] = False
  
  dfs([], [False] * n)
  return result

for t in permutations(numbers, m): print(*t)