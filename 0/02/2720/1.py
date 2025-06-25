coins = [25, 10, 5, 1]

for _ in range(int(input())):
  result = []
  c = int(input())

  for coin in coins:
    result.append(c // coin)
    c -= result[-1] * coin

  print(*result)