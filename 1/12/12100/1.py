from collections import deque
from copy import deepcopy
from sys import stdin
input = stdin.readline

MAX_COUNT = 5
DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def get_max(board): return max(map(max, board))

def merge(line, dir):
  removed = [cell for cell in line if cell][::-dir] + [0]
  merged = []

  rl = len(removed) - 1
  i = 0
  while True:
    if i < 0 or i >= rl: break
    value = removed[i]
    if value != removed[i + 1]: merged.append(value)
    else: merged.append(value << 1); i += 1
    i += 1

  return (merged + [0] * (n - len(merged)))[::-dir]


def move(board, dir):
  dr, dc = dir
  result = deepcopy(board)
  transposed = list(zip(*result))
  merged = []

  for i in range(n):
    if dc: result[i] = merge(result[i][:], dc); continue
    merged = merge(transposed[i][:], dr)
    transposed[i] = merged[:]
    result = list(zip(*transposed))

  return result


def play(board):
  max_value = 0
  stack = deque([(board, 0)])
  
  while stack:
    curr_board, count = stack.pop()
    if count == MAX_COUNT: continue

    for dir in DIRS:
      next_board = move(curr_board, dir)
      max_value = max(max_value, get_max(next_board))

      stack.append((next_board, count + 1))

  return max_value

print(play(board))