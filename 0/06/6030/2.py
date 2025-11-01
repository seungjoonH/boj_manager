from itertools import product
factors = lambda n: sorted(set(i for i in range(1, n + 1) if not (n % i)))
for x, y in product(*map(factors, map(int, input().split()))): print(f'{x} {y}')