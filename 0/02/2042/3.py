import math
from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())
numbers = [int(input()) for _ in range(n)]
segment = [0] * (2 ** (math.ceil(math.log2(n)) + 1))

def build(index=0, left=0, right=n - 1):
  if left == right: segment[index] = numbers[left]; return segment[index]

  mid = (left + right) // 2

  left_index, right_index = index * 2 + 1, index * 2 + 2

  build(left_index, left, mid)
  build(right_index, mid + 1, right)

  segment[index] = segment[left_index] + segment[right_index]
  return segment[index]


def adjust(i, delta, index=0, left=0, right=n - 1):
  segment[index] += delta
  if left == right: numbers[left] += delta; return

  mid = (left + right) // 2

  if left <= i <= mid: adjust(i, delta, index * 2 + 1, left, mid)
  else: adjust(i, delta, index * 2 + 2, mid + 1, right)


def get_sum(find_left, find_right, index=0, left=0, right=n - 1):
  if find_right < left or find_left > right: return 0
  elif find_left <= left <= right <= find_right: return segment[index]

  mid = (left + right) // 2

  return (
    get_sum(find_left, find_right, index * 2 + 1, left, mid) 
    + get_sum(find_left, find_right, index * 2 + 2, mid + 1, right)
  )

build()

for _ in range(m + k):
  a, b, c = map(lambda x: int(x) - 1, input().split())
  print(get_sum(b, c)) if a else adjust(b, c - numbers[b] + 1)