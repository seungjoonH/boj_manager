from collections import deque
n, ans = int(input()), [1]
dq = deque(range(1, n))

while dq:
  num = dq.popleft()
  dq.append(num)
  num = dq.popleft()
  ans.append(num + 1)

print(*ans)