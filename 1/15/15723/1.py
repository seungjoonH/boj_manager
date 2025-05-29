premises = [input().split(' is ') for _ in range(int(input()))]
conclusions = [input().split(' is ') for _ in range(int(input()))]

graph, visited = {}, []
for p1, p2 in premises: graph[p1] = p2

def search(node, find):
  if node == find: return 'T'
  if node not in graph or node in visited: return 'F'
  visited.append(node)
  return search(graph[node], find)

for c1, c2 in conclusions: 
  visited.clear()
  print(search(c1, c2))

'''
4
a is b
b is c
c is d
d is b
5
a is c
a is d
d is c
b is d
d is a
'''

'''
3
c is b
a is b
b is c
3
b is a
a is c
c is a
'''