i = [*open(0)]
def f(x): return ((s:=x.strip()) == '/') * s + s + s.isdigit() * ')'
print(eval('(' * (len(i) // 2) + ''.join(map(f, i[:-1]))))