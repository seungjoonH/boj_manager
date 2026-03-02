target = input()
visited = [0] * len(target)

def opening(s, l = 0, r = len(target)):
  if not s or l > r: return

  m = min(s)
  i = target.find(m, l, r)
  si = s.find(m)
  visited[i] = 1

  print(*[c for i, c in enumerate(target) if visited[i]], sep='')

  opening(s[si + 1:], i + 1, r)
  opening(s[:si], l, i)

opening(target)