from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
acc_sums, results = [0], []

for i in range(n):
  acc_sums.append(numbers[i] + acc_sums[i])

for _ in range(m):
  s, e = map(int, input().split())
  results.append(acc_sums[e] - acc_sums[s - 1])

print(*results, sep='\n')

'''
5 3
5 4 3 2 1
1 3
2 4
5 5
'''