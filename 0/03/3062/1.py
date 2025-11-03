def r(n): s = str(int(n) + int(n[::-1])); return ['NO', 'YES'][s == s[::-1]]
_, *a = map(str.strip, open(0)); print(*map(r, a), sep='\n')