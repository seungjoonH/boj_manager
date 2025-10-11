_, *a = map(int, open(0))
def f(n): q, r = divmod(n, 5); return ('++++ ' * q + '|' * r).strip()
print(*map(f, a), sep='\n')