n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
count = 0

for coin in coins[::-1]:
  if not k: break
  c = k // coin
  if not c: continue
  count += c
  k -= coin * c
  
print(count)