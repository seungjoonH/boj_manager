from functools import reduce
a=[*map(str.strip,open(0))][:-1]
def f(x,t):i,v=t;return i and(i%2 and x+'*'+v or x+'-'+v+')')or'('*int(v)+'1'
print(*[eval(reduce(f,enumerate(r.split()),''))for r in a],sep='\n')