def next_number(e1, e2=None, e3=None):
  if e1 == e2: return e1 if (e3 is None or e1 == e3) else 'B'
  if e2 is None or e3 is None: return 'A'
  
  a = (e3 - e2) / (e2 - e1)
  b = (e3 * e1 - e2 * e2) / (e1 - e2)

  if int(a) != a or int(b) != b: return 'B'
  return e3 * int(a) + int(b)

def test(n, v):
  for i in range(n):
    nn = next_number(*v[i:i + 3])
    if str(nn) in 'AB': return nn
    if i + 3 >= n: return nn
    elif nn != v[i + 3]: return 'B'

n = int(input())
v = list(map(int, input().split()))

print(test(n, v))