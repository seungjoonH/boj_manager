_, _, *a = map(str.strip, open(0))
r = [[*map(int, j.split()[1:])] for j in ' '.join(i or ',' for i in a).split(' , ')]
print(*[['YES', 'NO'][bool(sum(i) % len(i))] for i in r], sep='\n')