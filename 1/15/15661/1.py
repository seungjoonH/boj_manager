from itertools import combinations
from sys import stdin
input = stdin.readline

n = int(input())
powers = [[*map(int, input().split())] for _ in range(n)]
total = sum(map(sum, powers))

def get_combs(b): 
  return [*combinations([i for i, v in enumerate(b[::-1]) if int(v)], 2)]

minimum = float('inf')

for i in range(1, 2 ** n - 1):
  start, link = i, (2 ** n - 1) ^ i
  start_combs, link_combs = map(get_combs, [bin(start)[2:], bin(link)[2:]])
  start_power = sum(powers[a][b] + powers[b][a] for a, b in start_combs)
  link_power = sum(powers[a][b] + powers[b][a] for a, b in link_combs)
  minimum = min(minimum, abs(start_power - link_power))

print(minimum)