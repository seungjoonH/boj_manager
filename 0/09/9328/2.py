import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)
WALL, DOCS = '*$'

def is_door(c): return 64 < ord(c) < 91
def is_key(c): return 96 < ord(c) < 123

def testcase():
  h, w = map(int, input().split())
  mp = [list(input().rstrip()) for _ in range(h)]
  key_ipt = input().rstrip()

  def out_of_range(r, c): 
    return r not in range(h) or c not in range(w)

  def visit(r, c): mp[r][c] = WALL

  doors = dict()
  keys = set() if key_ipt == '0' else set(key_ipt)

  def add_door(door, coord):
    if door in doors: doors[door].add(coord)
    else: doors[door] = set([coord])

  def rem_door(door, coord):
    if door in doors:
      if len(door) == 1: doors.pop(door)
      else: doors[door].remove(coord)

  def find_door(key): 
    door = key.upper()
    if door in doors: return doors[door]
    return set()

  def has_key(door): return door.lower() in keys

  count = 0

  def bfs(r, c):
    nonlocal count
    queue = deque([(r, c)])

    while queue:
      cr, cc = queue.popleft()
      curr = mp[cr][cc]
      if is_door(curr): 
        add_door(curr, (cr, cc))
        if not has_key(curr): continue
      if curr == DOCS: count += 1
      visit(cr, cc)

      for dir in DIRS:
        dr, dc = dir
        nr, nc = cr + dr, cc + dc

        if out_of_range(nr, nc): continue
        v = mp[nr][nc]
        if v == WALL: continue
        if is_door(v):
          add_door(v, (nr, nc))
          if not has_key(v): continue
        if is_key(v): 
          keys.add(v)
          found = find_door(v).copy()
          for coord in found:
            if find_door(v): continue
            bfs(*coord)
            rem_door(v.upper(), coord)
          
        queue.append((nr, nc))

  for i in range(h):
    if mp[i][0] != WALL: bfs(i, 0)
    if mp[i][-1] != WALL: bfs(i, w - 1)

  for i in range(1, w - 1):
    if mp[0][i] != WALL: bfs(0, i)
    if mp[-1][i] != WALL: bfs(h - 1, i)

  for d in doors.copy():
    before_keys = keys.copy()
    for nr, nc in doors[d]: 
      if has_key(d):
        bfs(nr, nc)
        rem_door(d, (nr, nc))

    new_keys = keys - before_keys
    
    for k in new_keys:
      found = find_door(k).copy()
      for coord in found:
        bfs(*coord)
        rem_door(k.upper(), coord)

  return count

for _ in range(int(input())): print(testcase())