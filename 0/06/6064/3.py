import math
from sys import stdin
input = stdin.readline

def cain(m, n, x, y):
  lcm = m * n / math.gcd(m, n)
  for i in range(n):
    c = i * m + x
    if c > lcm: break
    if (c - 1) % n + 1 == y: return c
  return -1

for _ in range(int(input())):
  print(cain(*map(int, input().split())))