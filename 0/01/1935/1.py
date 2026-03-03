from collections import deque

OPERATORS = '+-*/'
n = int(input())
expr = input()
values = {chr(65 + i): float(input()) for i in range(n)}
stack = deque()

def calculate(a, b, op): return eval(str(b) + op + str(a))

for op in expr:
  if op in OPERATORS:
    result = calculate(stack.pop(), stack.pop(), op)
    stack.append(result)
    continue

  value = values[op] if op in values else op
  stack.append(value)

print('%.2f' % stack.pop())