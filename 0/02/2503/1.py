l = [str(i) for i in range(123, 988) if len(set(str(i))) == 3 and '0' not in set(str(i))]

def strike(x, y): return sum(a == b for a, b in zip(x, y))
def ball(x, y): return sum(i in set(y) for i in set(x)) - strike(x, y)

def filt(l, x, s, b):
  return [*filter(lambda e: strike(e, x) == s and ball(e, x) == b, l)]

ret = l[:]

for _ in range(int(input())):
  x, s, b = map(int, input().split())
  ret = filt(ret, str(x), s, b)

print(len(ret))