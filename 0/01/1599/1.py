_, *a = map(str.strip, open(0))
d = dict(zip('abkdeghilmn#oprstuwy',range(20)))
key = lambda x: [*map(lambda y: d[y], x.replace('ng','#'))]
print(*sorted(a, key=key), sep='\n')