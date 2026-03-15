from itertools import combinations
from sys import stdin
input = stdin.readline

n = int(input())
powers = [[*map(int, input().split())] for _ in range(n)]
total = sum(map(sum, powers))

memo = dict()

def get_power(index):
  if index in memo: return memo[index]
  combs = [*combinations([i for i, v in enumerate(bin(index)[2:][::-1]) if int(v)], 2)]
  power = sum(powers[a][b] + powers[b][a] for a, b in combs)
  memo[index] = power
  return power

minimum = float('inf')

for i in range(1, 2 ** n - 1):
  start, link = i, (2 ** n - 1) ^ i
  start_power, link_power = map(get_power, [i, (2 ** n - 1) ^ i])
  minimum = min(minimum, abs(start_power - link_power))

print(minimum)