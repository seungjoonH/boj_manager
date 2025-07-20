import math
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
pairs = [tuple(map(int, input().split())) for _ in range(m)]

size = 2 ** (math.ceil(math.log2(n)) + 1)
min_segment = [0] * size
max_segment = [0] * size


def build(index=0, low=0, high=n - 1):
  if low == high:
    min_segment[index] = numbers[low] 
    max_segment[index] = numbers[low]
    return (min_segment[index], max_segment[index])
  
  mid = (low + high) // 2

  left_index, right_index = index * 2 + 1, index * 2 + 2
  build(left_index, low, mid)
  build(right_index, mid + 1, high)

  min_segment[index] = min(min_segment[left_index], min_segment[right_index])
  max_segment[index] = max(max_segment[left_index], max_segment[right_index])

  return min_segment[index], max_segment[index]


def get_minmax(left, right, index=0, low=0, high=n - 1):
  if right < low or left > high: return float('INF'), -float('INF')
  if left <= low <= high <= right: return min_segment[index], max_segment[index]

  mid = (low + high) // 2

  left_min, left_max = get_minmax(left, right, 2 * index + 1, low, mid)
  right_min, right_max = get_minmax(left, right, 2 * index + 2, mid + 1, high)

  return min(left_min, right_min), max(left_max, right_max)

build()

for a, b in pairs: print(*get_minmax(a - 1, b - 1))