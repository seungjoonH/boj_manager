input(); s = input()
def isin(t): return all(map(lambda x: x in s, t))
a, b = map(isin, ['roygbiv', 'ROYGBIV'])
print(['NO!', 'yes', 'YES', 'YeS'][a + 2 * b])