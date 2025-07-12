from collections import deque
from sys import stdin, setrecursionlimit
input = stdin.readline

setrecursionlimit(10 ** 6)

input()
liquids = deque(map(int, input().split()))
minimum = float('INF')
pair = []

def find(array, number, low=0, high=None):
  if high is None: high = len(array) - 1
  if high < low: return 
  mid = (low + high) // 2

  global minimum, pair
  mid_number = array[mid]
  diff = abs(mid_number + number)
  if minimum > diff: minimum = diff; pair = [number, mid_number]
  if not minimum: return

  find(array, number, low, mid - 1)
  find(array, number, mid + 1, high)

while liquids:
  number = liquids.popleft()
  find(liquids, number)

print(*pair)