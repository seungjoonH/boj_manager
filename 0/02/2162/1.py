from sys import stdin
input = stdin.readline

def sign(n):
  if not n: return 0
  return 1 - 2 * (n < 0)

def ccw(p1, p2, p3):
  p12 = p1.subtract(p2)
  p13 = p1.subtract(p3)
  cp = p12.cross_product(p13)
  return sign(cp.z)

class Point:
  def __init__(self, x, y, z=0):
    self.x = x
    self.y = y
    self.z = z
  
  def subtract(self, other):
    return Point(
      self.x - other.x, 
      self.y - other.y,
      self.z - other.z
    )

  def cross_product(self, other):
    return Point(
      self.y * other.z - self.z * other.y,
      self.z * other.x - self.x * other.z,
      self.x * other.y - self.y * other.x
    )


class Line:
  def __init__(self, start, end):
    self.start = start
    self.end = end
  
  def to_list(self):
    return self.start, self.end
  
  def meet_with(self, other):
    p1, p2 = self.to_list()
    p3, p4 = other.to_list()
    
    p123 = ccw(p1, p2, p3)
    p124 = ccw(p1, p2, p4)
    p341 = ccw(p3, p4, p1)
    p342 = ccw(p3, p4, p2)

    if p123 * p124 == 0 and p341 * p342 == 0:
      x_met = max(p1.x, p2.x) < min(p3.x, p4.x) or min(p1.x, p2.x) > max(p3.x, p4.x)
      y_met = max(p1.y, p2.y) < min(p3.y, p4.y) or min(p1.y, p2.y) > max(p3.y, p4.y)
      if p1.x == p4.x: return not y_met
      if p1.y == p4.y: return not x_met
      return not (x_met and y_met)
    return p123 * p124 <= 0 and p341 * p342 <= 0

class DisjointSet:
  def __init__(self, n):
    self.parents = list(range(n))
    self.ranks = [1] * n
  
  def find_root(self, node):
    if self.parents[node] != node:
      self.parents[node] = self.find_root(self.parents[node])
    return self.parents[node]

  def union(self, a, b):
    root_a = self.find_root(a)
    root_b = self.find_root(b)
    rank_a = self.ranks[root_a]
    rank_b = self.ranks[root_b]

    if root_a != root_b:
      if rank_a > rank_b: self.parents[root_b] = root_a
      elif rank_a < rank_b: self.parents[root_a] = root_b
      else:
        self.parents[root_b] = root_a
        self.ranks[root_a] += 1

n = int(input())
lines = []

for _ in range(n):
  a, b, c, d = map(int, input().split())
  lines.append(Line(Point(a, b), Point(c, d)))

graph = [[] for _ in range(n)]

for i in range(n):
  for j in range(n):
    if i == j: continue
    if lines[i].meet_with(lines[j]):
      graph[i].append(j)

ds = DisjointSet(n)

for node in range(n):
  for child in graph[node]:
    ds.union(node, child)

l = [ds.find_root(i) for i in range(n)]
s = set(l)

print(len(s))
print(max([l.count(i) for i in s]))

'''
8
1 1 3 3
2 1 2 3
3 1 1 3
3 2 1 2
4 1 4 3
1 4 3 4
1 5 3 5
2 4 2 6
'''