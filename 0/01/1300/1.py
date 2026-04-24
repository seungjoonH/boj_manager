n, k = map(int, open(0))
left, right = 1, k

result = 0

while left <= right:
  mid = (left + right) // 2
  s = sum(min(mid // i, n) for i in range(1, n + 1))
  if k > s: left = mid + 1
  else: right = mid - 1; result = mid

print(result)