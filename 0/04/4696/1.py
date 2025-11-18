*a, _ = map(str.strip, open(0))
print('\n'.join('%.2f' % sum(float(k) ** i for i in range(5)) for k in a))