n = int(input()); w = 2 * n - 1
print(*[('*' * (2 * abs(i - n + 1) + 1)).center(w).rstrip() for i in range(w)], sep='\n')