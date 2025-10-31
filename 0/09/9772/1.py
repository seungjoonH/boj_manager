s = lambda x: (x > 0) - (x < 0)
def q(t): c = [*map(s, map(float, t))]; return 'AXIS' * (0 in c) or 'Q' + ' 4132'[sum(c) // 2 + c[0]]
print(*map(q, map(str.split, open(0))), sep='\n')