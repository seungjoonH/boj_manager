while True:
  a, b = map(int, input().split())
  if a or b: print(['multiple', 'factor', 'neither'][2 * bool(a % b) + bool(b % a) - 1])
  else: break