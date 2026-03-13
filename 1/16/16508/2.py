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
def shift(a, i): return a[i:] + a[:i]

costs_copy = copy(costs)
cost_list = [*costs.keys()]
minimum = MAX

for i in range(len(costs)):
  chosen = [-1 for _ in t]
  costs = copy(costs_copy)
  shifted = shift(cost_list, i)
  
  for j, c in enumerate(t):
    for cost in shifted:
      if c in costs[cost]:
        chosen[j] = cost_list.index(cost)
        costs[cost].remove(c)
        break
  
  if any([k == -1 for k in chosen]): continue
  minimum = min(minimum, sum(cost_list[k] for k in set(chosen)))

print(-1 if minimum == MAX else minimum)