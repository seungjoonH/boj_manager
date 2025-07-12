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
  s = mid_number + number
  if minimum > abs(s): minimum = abs(s); pair = [number, mid_number]
  
  if s > 0: find(array, number, low, mid - 1)
  elif s < 0: find(array, number, mid + 1, high)
  else: return

while liquids:
  number = liquids.popleft()
  find(liquids, number)

print(*pair)