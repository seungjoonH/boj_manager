target = input()
visited = [0] * len(target)

def opening(s, l = 0, r = len(target)):
  if not s or l > r: return s

  m = min(s)
  i = target.find(m, l, r)
  mi = s.find(m)
  visited[i] = 1

  print(*[c for i, c in enumerate(target) if visited[i]], sep='')

  right = opening(s[mi + 1:], i + 1, r)
  return opening(s[:mi], l, i) + s[mi] + right

opening(target)