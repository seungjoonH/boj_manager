import math
from sys import stdin
input = stdin.readline
t = int(input())
f = math.factorial
def c(n, r): return f(n) // f(r) // f(n - r)

for i in range(t):
  n, m = map(int, input().split())
  print(c(m, n))