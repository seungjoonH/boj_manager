_, *a = map(str.split, open(0))
for i, r in enumerate(a): print(f'Case #{i + 1}:', max(map(int, r)))