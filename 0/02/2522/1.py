n = 2 * int(input()) - 1
print(*[' ' * abs(n // 2 - i) + '*' * min(i + 1, n - i) for i in range(n)], sep='\n')