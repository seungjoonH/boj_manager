def remove_node(tree, remove):
  removed_tree = dict(tree)
  removed_tree.pop(remove)
  
  for node, parent in removed_tree.items():
    if parent == remove:
      removed_tree = remove_node(removed_tree, node)

  return removed_tree

def count_leaves(tree):
  return sum(i not in tree.values() for i in tree)

input()
tree = dict(enumerate(map(int, input().split())))
remove = int(input())

tree = remove_node(tree, remove)
count = count_leaves(tree)

print(count)
