def exercise():
  N, m, M, T, R = map(int, input().split())

  if m + T > M: return -1
  X = m; i = t = 0
  while 1:
    if t == N: return i
    if X + T > M: X = max(m, X - R)
    else: X += T; t += 1
    i += 1
  return -1

print(exercise())