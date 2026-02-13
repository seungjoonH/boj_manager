from heapq import *

def median(arr):
  medians = []
  l, r = [], []

  for i, v in enumerate(arr):
    if not len(l): heappush(l, -v)
    else:
      m = -l[0]
      if m < v: heappush(r, v)
      else: heappush(l, -v)

    heapify(l), heapify(r)

    if len(l) < len(r): heappush(l, -heappop(r))
    elif len(l) > 1 + len(r): heappush(r, -heappop(l))
  
    if not i % 2: medians.append(-l[0])

  return medians

_, *a = open(0)
arr, n = [], 0

isnum = True

for ipt in a:
  s = ipt.split()

  if isnum:
    n = int(ipt) 
    arr = []
    isnum = False
    continue

  arr.extend([*map(int, s)])

  if len(arr) == n: 
    medians = median(arr)
    size = len(medians)
    print(size)
    for i in range(0, size, 10): print(*medians[i:i + 10])
    isnum = True