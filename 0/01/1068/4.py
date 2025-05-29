from collections import deque

def remove_node(tree, remove):
  children = tree.pop(remove)
  for child in children:
    remove_node(tree, child)
  return tree

def count_leaves(tree):
  return sum(map(lambda c: len(c) == 0, tree.values()))

n = int(input())
parent_tree = dict(enumerate(map(int, input().split())))
tree = dict(enumerate([[] for _ in range(n + 1)], -1))
remove = int(input())

for node, parent in enumerate(parent_tree.values()):
  tree[parent].append(node)

tree = remove_node(tree, remove)

print(tree)

count = count_leaves(tree)

print(count)
