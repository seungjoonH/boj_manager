x, y, z = map(int, input().split())
print(max(x // y * z, x * y // z))