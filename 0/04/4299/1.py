a, b = map(int, input().split())
x, y = (a + b) // 2, (a - b) // 2
print(*[[-1], [x, y]][a >= b and a == x + y and b == x - y])