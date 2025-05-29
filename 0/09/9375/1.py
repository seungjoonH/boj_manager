from itertools import combinations as C
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
  n = int(input())
  
  categories = []
  for __ in range(n): categories.append(input().split()[-1])

  result = n

  for r in range(2, n + 1):
    result += list(map(len, map(set, C(categories, r)))).count(r)
  
  print(result)