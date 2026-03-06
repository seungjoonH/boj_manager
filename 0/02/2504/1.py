from collections import deque

stack = deque()
expr = input()

def isint(x):
  try: int(x); return True
  except: return False

def xyz():
  n = len(stack)
  x = stack[-3] if n >= 3 else '#'
  y = stack[-2] if n >= 2 else '#'
  z = stack[-1] if n >= 1 else '#'
  return x, y, z

def pop(n): 
  for _ in range(n): stack.pop()

for p in expr:
  stack.append(p)
  
  while True:
    x, y, z = xyz()

    if z in '[(': break
    if isint(y + z): pop(2); stack.append(str(int(y) + int(z)))
    elif y + z == '()': pop(2); stack.append('2')
    elif y + z == '[]': pop(2); stack.append('3')
    elif x + z == '()' and isint(y): pop(3); stack.append(str(2 * int(y)))
    elif x + z == '[]' and isint(y): pop(3); stack.append(str(3 * int(y)))
    else: break

result = ''.join([*stack])
print(result if isint(result) else 0)