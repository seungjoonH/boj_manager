n = str(eval('*'.join(map(str.strip, open(0)))))
d = dict(sorted(zip(map(int, n), map(n.count, n))))
for i in range(10): print(d[i] if i in d else 0)