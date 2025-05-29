from collections import Counter
from itertools import combinations
from math import factorial as f
from math import prod
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
  result = n = int(input())
  categories = [input().split()[-1] for __ in range(n)]
  counts = Counter(categories).values()

  for r in range(2, n + 1):
    if len(counts) < r: continue
    result += sum(map(prod, combinations(counts, r)))

  print(result)


'''
1
7
a A
b B
c C
d B
e C
f B
g D
'''