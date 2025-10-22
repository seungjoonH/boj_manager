_, *a = map(str.split, open(0))
print(*[f'Case {i + 1}: {eval(v)}' for i, v in enumerate(map('+'.join, a))], sep='\n')