(x1, y1), (x2, y2) = map(lambda x: divmod(x - 1, 4), map(int, input().split()))
print(abs(x2 - x1) + abs(y2 - y1))