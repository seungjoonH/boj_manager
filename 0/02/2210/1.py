board = [input().replace(' ', '') for _ in range(5)]
numbers = set()

def start(board, x, y, number=''):
  if len(number) == 6: return set([number])
  sub_set = set()

  for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    if x + dx not in range(5): continue
    if y + dy not in range(5): continue
    sub_set |= start(board, x + dx, y + dy, number + board[x][y])
  return sub_set

for i in range(5):
  for j in range(5):
    numbers |= start(board, i, j)

print(len(numbers))