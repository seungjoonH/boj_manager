_, *a = map(str.strip, open(0))
print(*[f'{int(i)} is ' + ['even','odd'][int(i) % 2] for i in a], sep='\n')
