l = sorted(map(lambda x: x[0], open(0)))
d = dict(zip(l, map(l.count, l)))
f = [*filter(lambda x: d[x] > 4, d)]
print(''.join(['PREDAJA' * (not len(f)), *f]))