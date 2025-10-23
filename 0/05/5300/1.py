n = int(input())
def r(s, e): return ' '.join(map(str, range(s + 1, e + 1)))
print(*[r(6 * i, 6 * (i + 1)) for i in range(n // 6)], sep=' Go! ', end='')
print((n >= 6) * ' Go! ' + (n % 6 and (r(n - n % 6, n) + ' Go!') or ''))