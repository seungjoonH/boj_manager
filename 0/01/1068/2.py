from collections import deque

def remove_node(tree, remove):
  removed_tree = dict(tree)
  removed_tree.pop(remove)
  queue = deque([remove])

  while queue:
    parent = queue.popleft()
    
    for node in tree:
      if tree[node] == parent:
        removed_tree.pop(node)
        queue.append(node)

  return removed_tree

def count_leaves(tree):
  return sum(i not in tree.values() for i in tree)

input()
tree = dict(enumerate(map(int, input().split())))
remove = int(input())

tree = remove_node(tree, remove)
count = count_leaves(tree)

print(count)
