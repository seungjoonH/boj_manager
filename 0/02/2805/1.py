from sys import *
input = stdin.readline

n, m = map(int, input().split())
trees = sorted(list(map(int, input().split())), reverse=True)

def get_quantity(height):
  return sum(map(lambda x: max(x - height, 0), trees))

cache = dict()
def binary_search(low=0, high=trees[0]):
  mid = (high + low) // 2
  quantity = get_quantity(mid)
  
  if mid + 1 in cache: 
    if quantity > m > cache[mid + 1]:
      return mid

  cache[mid] = quantity

  if quantity > m: return binary_search(mid + 1, high)
  elif quantity < m: return binary_search(low, mid - 1)
  return mid

print(binary_search())