import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]

DIRS = (1, 0), (0, 1), (-1, 0), (0, -1)
def out_of_range(x, y): return y not in range(n) or x not in range(m)

def get_area(x, y):
  area = 0
  def _dfs(x, y): 
    nonlocal area
    if not paper[y][x]: return
    paper[y][x] = 0
    area += 1

    for dir in DIRS:
      dx, dy = dir
      nx, ny = x + dx, y + dy
      if out_of_range(nx, ny): continue
      _dfs(nx, ny)

  _dfs(x, y)
  return area

c = mx = 0
for i in range(n):
  for j in range(m):
    if not paper[i][j]: continue
    area = get_area(j, i)
    if not area: continue
    c += 1
    mx = max(mx, area)

print(c, mx, sep='\n')