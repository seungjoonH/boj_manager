a = [*map(chr, range(97, 123))]
s1, s2 = input(), input()
d1 = {i: s1.count(i) for i in a}
d2 = {i: s2.count(i) for i in a}
print(sum(abs(d1[i] - d2[i]) for i in a))