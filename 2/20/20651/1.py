from itertools import combinations_with_replacement as cwr

n = int(input())
flowers = [*map(int, input().split())]

def count_avg(i, j):
  if i == j: return True
  l = flowers[i - 1:j]
  return (sum(l) / len(l)) in l

print(sum(count_avg(*t) for t in cwr(range(1, n + 1), 2)))