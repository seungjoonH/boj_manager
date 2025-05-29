from collections import Counter
from math import prod
from sys import stdin
input = stdin.readline

for _ in range(int(input())):
  n = int(input())
  categories = [input().split()[-1] for __ in range(n)]
  counts = Counter(categories).values()
  print(prod(map(lambda x: x + 1, counts)) - 1)

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