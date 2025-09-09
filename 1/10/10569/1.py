def area(v, e): return 2 - v + e
print(*[area(*map(int, input().split())) for _ in range(int(input()))], sep='\n')