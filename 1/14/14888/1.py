# 연산자 끼워넣기
# 맞았습니다!!
# https://www.acmicpc.net/source/88971807

from sys import stdin
input = stdin.readline

n = int(input())
numbers = input().split()
operators = dict(zip('+-*/', list(map(int, input().split()))))
mini = 1+10e8
maxi = -mini

def dfs(operators, index=0, number=numbers[0]):
  if index == n - 1:
    global maxi, mini
    maxi = max(maxi, number)
    mini = min(mini, number)
    return
  
  a, b = number, numbers[index + 1]

  for op, count in operators.items():
    ops = dict.copy(operators)
    if not count: continue

    ops[op] = count - 1
    next_number = eval(f'int({a}{op}{b})')
    dfs(ops, index + 1, next_number)

dfs(operators)

print(maxi)
print(mini)