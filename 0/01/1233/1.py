from itertools import product
l = [*map(sum, product(*map(range, map(int, input().split()))))]
d = dict(zip(l, map(l.count, l)))
print(3 + min(map(lambda x: x[0], filter(lambda x: x[1] == max(d.values()), d.items()))))