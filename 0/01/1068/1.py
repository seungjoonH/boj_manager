import copy

n = int(input())
tree = dict(enumerate(map(int, input().split())))
remove = int(input())
node_set = set()

tree.pop(remove)
node_set.add(remove)

while node_set:
  temp = copy.deepcopy(tree)
  parent = node_set.pop()

  for i in tree:
    if tree[i] == parent:
      temp.pop(i)
      node_set.add(i)

    tree = temp

count = 0

for i in tree:
  count += i not in tree.values()

print(count)