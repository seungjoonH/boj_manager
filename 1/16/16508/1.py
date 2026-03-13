from sys import stdin
input = stdin.readline

MAX = float('inf')
t = input().strip()
n = int(input())

chosen = [-1 for _ in t]
costs = dict()

for _ in range(n):
  cost, title = input().split()
  cost = int(cost)
  costs[cost] = sorted(''.join(c * title.count(c) for c in set(t)))

def copy(d): return {k: v[:] for k, v in d.items()}

costs_copy = copy(costs)
minimum = MAX

for j in range(len(costs)):
  chosen = [-1 for _ in t]
  costs = copy(costs_copy)
  
  for i, c in enumerate(t):
    cost_list = [*costs.keys()]
    cost_list = cost_list[j:] + cost_list[:j]

    for k, cost in enumerate(cost_list):
      if c in costs[cost]: chosen[i] = k; costs[cost].remove(c)

  if any([i == -1 for i in chosen]): continue
  minimum = min(minimum, sum(cost_list[i] for i in set(chosen)))

print(-1 if minimum == MAX else minimum)
