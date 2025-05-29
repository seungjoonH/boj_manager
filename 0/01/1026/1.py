from sys import stdin
input = stdin.readline

n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()), reverse=True)
print(eval('+'.join(f'{a[i]}*{b[i]}' for i in range(n))))