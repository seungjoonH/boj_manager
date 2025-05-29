from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
mp = [list(map(int, input().split())) for _ in range(n)]
print(mp)