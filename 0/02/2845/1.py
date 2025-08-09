n = eval(input().replace(' ', '*'))
print(*map(lambda x: int(x) - n, input().split()))