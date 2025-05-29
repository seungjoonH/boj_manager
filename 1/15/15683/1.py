n, m = map(int, input().split())
office = [input().split() for _ in range(n)]

BLANK, WALL, WATCHED = '06#'
L, T, R, B = (0, -1), (-1, 0), (0, 1), (1, 0)

cctvs = [[],
  [[L], [T], [R], [B]],
  [[L, R], [T, B]],
  [[L, T], [T, R], [R, B], [B, L]],
  [[L, T, R], [T, R, B], [R, B, L], [B, L, T]],
  [[L, T, R, B]],
]

def copy(mat): return [row[:] for row in mat]
def encode(mat): return ';'.join(','.join(row) for row in mat)
def decode(code): return [row.split(',') for row in code.split(';')]

def out_of_range(r, c): return r not in range(n) or c not in range(m)
def count_blanks(office): return sum(row.count(BLANK) for row in office)

def watch(office, position, direction):
  copied = copy(office)
  r, c = position; dr, dc = direction; dist = 0
  while True:
    dist += 1
    offset_r, offset_c = r + dist * dr, c + dist * dc
    if out_of_range(offset_r, offset_c): break
    target = copied[offset_r][offset_c]

    if target == WALL: break
    if target != BLANK: continue
    copied[offset_r][offset_c] = WATCHED
  
  return copied

targets = []

for r in range(n):
  for c in range(m):
    target = office[r][c]
    if target in [BLANK, WALL]: continue
    targets.append([target, (r, c)])

targets.sort(key=lambda x: '52431'.index(x[0]))

watched_set = set([encode(office)])

for index, pos in targets:
  r, c = pos
  cctv = cctvs[int(index)]
  sub_set = set()
  
  while watched_set:
    popped = decode(watched_set.pop())

    for rotated in cctv:
      watched = copy(popped)
      if L in rotated: watched = watch(watched, pos, L)
      if T in rotated: watched = watch(watched, pos, T)
      if R in rotated: watched = watch(watched, pos, R)
      if B in rotated: watched = watch(watched, pos, B)
      sub_set.add(encode(watched))

  watched_set = set(sub_set)

print(min(map(count_blanks, watched_set)))

'''

8 8
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1

'''