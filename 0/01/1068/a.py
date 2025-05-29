# def count_leaves(tree):
#   count = 0
#   for i in tree:
#     count += i not in tree.values()
  
#   return count

def count_leaves(tree):
  return sum(i not in tree.values() for i in tree)


tree = dict(enumerate(map(int, input().split())))

print(count_leaves(tree))
