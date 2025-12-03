p, k = map(int, input().split())

def password():
  for i in range(2, k):
    if not p % i: return f'BAD {i}'
  return 'GOOD'

print(password())
