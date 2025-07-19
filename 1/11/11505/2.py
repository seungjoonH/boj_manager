import math
from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
LP = 1_000_000_007

size = 2 ** (math.ceil(math.log2(n)) + 1)
segment = [0] * size

def prod(a, b): return ((a % LP) * (b % LP)) % LP

def build(index=0, left=0, right=n - 1):
  if left == right: segment[index] = numbers[left]; return segment[index]

  mid = (left + right) // 2

  left_index, right_index = index * 2 + 1, index * 2 + 2

  build(left_index, left, mid)
  build(right_index, mid + 1, right)

  segment[index] = prod(segment[left_index], segment[right_index])
  return segment[index]


def adjust(i, after, index=0, left=0, right=n - 1):
  if left == right:
    numbers[i] = segment[index] = after
    return after

  mid = (left + right) // 2

  if left <= i <= mid: adjust(i, after, index * 2 + 1, left, mid)
  else: adjust(i, after, index * 2 + 2, mid + 1, right)

  segment[index] = prod(segment[index * 2 + 1], segment[index * 2 + 2])
  return segment[index]


def get_prod(find_left, find_right, index=0, left=0, right=n - 1):
  if find_right < left or find_left > right: return 1
  elif find_left <= left <= right <= find_right: return segment[index]

  mid = (left + right) // 2

  return prod(
    get_prod(find_left, find_right, index * 2 + 1, left, mid),
    get_prod(find_left, find_right, index * 2 + 2, mid + 1, right),
  )

build()

for _ in range(m + k):
  a, b, c = map(lambda x: int(x) - 1, input().split())
  print(get_prod(b, c)) if a else adjust(b, c + 1)