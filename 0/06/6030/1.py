from itertools import product
factors = lambda n: [1, *(i for i in range(2, 1 + n // 2) if not (n % i)), n]
for x, y in product(*map(factors, map(int, input().split()))): print(f'{x} {y}')