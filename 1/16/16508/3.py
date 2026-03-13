from sys import stdin
input = stdin.readline

MAX = float('inf')
t = input().strip()
n = int(input())

chosen = [-1 for _ in t]

cost_list = []
costs = []

for _ in range(n):
  cost, title = input().split()
  cost = int(cost)

  cost_list.append(cost)
  costs.append(sorted(''.join(c * title.count(c) for c in set(t))))

def copy(arr): return [v[:] for v in arr]
def shift(a, i): return a[i:] + a[:i]

costs_copy = copy(costs)
minimum = MAX

for i in range(n):
  chosen = [-1 for _ in t]
  costs = copy(costs_copy)
  shifted = shift(list(range(n)), i) 
  
  for j, c in enumerate(t):
    for idx in shifted:
      if c in costs[idx]:
        chosen[j] = idx
        costs[idx].remove(c)
        break
  
  if any(k == -1 for k in chosen): continue
  minimum = min(minimum, sum(cost_list[k] for k in set(chosen)))

print(-1 if minimum == MAX else minimum)