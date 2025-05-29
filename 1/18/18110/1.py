from sys import stdin
input = stdin.readline

n = int(input())
if not n: print(0); exit(0)

difficulties = sorted([int(input()) for _ in range(n)])
trim_count = round(n * .15)
_from, _to = trim_count, n - trim_count + 1

trimmed = difficulties[_from:_to]

print(difficulties)
print(trimmed)
print(_from, _to, '#')
difficulty = round(sum(trimmed) / len(trimmed))

print(difficulty)