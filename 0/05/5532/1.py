import math
from sys import stdin
l, a, b, c, d = map(int, stdin.readlines())
print(max(l - max(math.ceil(a / c), math.ceil(b / d)), 0))