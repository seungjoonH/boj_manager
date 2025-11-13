x, y, z = map(int, input().split())
print(int(max(x / y * z, x * y / z)))