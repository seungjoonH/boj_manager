_, *a = map(str, open(0))
print(*[['no', 'yes'][6 < len(i) < 11] for i in a], sep='\n')