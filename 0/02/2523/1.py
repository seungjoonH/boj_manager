n = 2 * int(input()) - 1
print(*['*' * min(i + 1, n - i) for i in range(n)], sep='\n')