v, *m = map(str.strip, open(0))
r, c = map(int, v.split())

x = [i.count('.') for i in m].count(c)
y = [i.count('.') for i in zip(*m)].count(r)

print(max(x, y))