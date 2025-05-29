from itertools import combinations as C
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
  result = n = int(input())
  categories = [input().split()[-1] for __ in range(n)]

  for r in range(2, n + 1):
    for e in list(C(categories, r)):
      result += len(set(e)) == r
  
  print(result)