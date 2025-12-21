_, *a = map(str.strip, open(0))

for s in a:
  l, x, y = len(s), s[::2], s[1:][::2]
  print(x + y if l % 2 else x)
  print(y + x if l % 2 else y)