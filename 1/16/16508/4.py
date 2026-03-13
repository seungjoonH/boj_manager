from itertools import combinations
from sys import stdin
input = stdin.readline

MAX = float('inf')
t = input().strip()
n = int(input())
costs = []
titles = []

for _ in range(n):
  cost, title = input().split()
  costs.append(int(cost))
  titles.append(title)

book_ids = [*range(n)]

groups = []

for i in range(n):
  groups.extend([*combinations(book_ids, i + 1)])

info = {c: t.count(c) for c in t}
minimum = MAX

for group in groups:
  chars = {chr(65 + i): 0 for i in range(26)}
  cost = 0

  for book_id in group: 
    cost += costs[book_id]
    for c in titles[book_id]: chars[c] += 1
  
  if all(chars[ch] >= cnt for ch, cnt in info.items()):
    minimum = min(minimum, cost)

print(-1 if minimum == MAX else minimum)