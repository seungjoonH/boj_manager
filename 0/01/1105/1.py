l, r = map(int, input().split())

t = l
for i, n in enumerate(str(l)[::-1]):
  if n != '8': continue
  if l + 10 ** i <= r: t += 10 ** i

print(str(t).count('8'))