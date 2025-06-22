import sys
from copy import deepcopy
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

sudoku = [list(map(int, input().split())) for _ in range(9)]

rows, cols, blocks = [], [], []

for i in range(9):
  row_value = col_value = 0
  for j in range(9):
    a, b = sudoku[i][j], sudoku[j][i]
    if a: row_value += 1 << (a - 1)
    if b: col_value += 1 << (b - 1)
  rows.append(row_value)
  cols.append(col_value)

for i in range(3):
  for j in range(3):
    block_value = 0
    for k in range(9):
      v = sudoku[3 * i + k // 3][3 * j + k % 3]
      if v: block_value += 1 << (v - 1)
    blocks.append(block_value)

result = deepcopy(sudoku)

def available(r, c, number):
  n = 1 << (number - 1)
  if n & rows[r]: return False
  if n & cols[c]: return False
  if n & blocks[(r // 3) * 3 + c // 3]: return False
  return True

def apply(r, c, number):
  n = 1 << (number - 1)
  rows[r] |= n
  cols[c] |= n
  blocks[(r // 3) * 3 + c // 3] |= n
  result[r][c] = number

def rollback(r, c, number):
    n = 1 << (number - 1)
    rows[r] &= ~n
    cols[c] &= ~n
    blocks[(r // 3) * 3 + c // 3] &= ~n
    result[r][c] = 0

def dfs(offset=0):
  if offset == 9 ** 2: return True
  r, c = divmod(offset, 9)
  
  if result[r][c]: return dfs(offset + 1)

  for number in range(1, 10):
    if available(r, c, number):
      apply(r, c, number)
      if dfs(offset + 1): return True
      rollback(r, c, number)
  return False

dfs()

for row in result: print(*row)