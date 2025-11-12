_,*a=open(0)
def f(x, y): return x // y + bool(x % y)
print(*[f(*map(int, i.split())) for i in a], sep='\n')