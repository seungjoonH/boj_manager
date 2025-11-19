l = [*range(1, 1 + int(input()))]
while len(l) > 1:
  l = [i[1] for i in filter(lambda t: t[0] % 2, enumerate(l))]
print(l[0])