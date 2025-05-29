def power(a, b, c):
  if b == 1: return a % c
  return power(a, b // 2, c) * power(a, b // 2 + (b & 1), c) % c
print(power(*map(int, input().split())))