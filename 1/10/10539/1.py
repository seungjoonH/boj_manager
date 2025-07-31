n = int(input())
avgs = list(map(int, input().split()))
accs = [0] + [(i + 1) * x for i, x in enumerate(avgs)]
numbers = [accs[i + 1] - accs[i] for i in range(n)]
print(*numbers)