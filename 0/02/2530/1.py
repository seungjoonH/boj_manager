t, d = map(int, input().split()), int(input())
def to_value(y, m, s): return y * 3600 + m * 60 + s
def from_value(v): return v // 3600 % 24, v % 3600 // 60, v % 60
print(*from_value(to_value(*t) + d))