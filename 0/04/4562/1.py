_, *a = map(str.split, open(0))
def f(s): x, y = map(int, s); return ['MMM', 'NO'][x < y] + ' BRAINS'
print(*map(f, a), sep='\n')