trees = [*map(str.strip, open(0))]
total = len(trees)
counts = {tree: 0 for tree in trees}

while trees: counts[trees.pop()] += 1

for t, c in sorted(counts.items()): 
  print(f'{t} {100 * c / total:.4f}' )