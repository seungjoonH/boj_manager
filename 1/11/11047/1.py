n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

def get_count(value, coins):
  v, c = value, 0
  for coin in coins[::-1]:
    while v >= coin:
      v -= coin; c += 1
      if not v: return c
  return c
  
print(get_count(k, coins))