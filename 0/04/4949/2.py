from collections import deque

def check_brackets(text):
  stack = deque()
  for ch in text:
    if ch in '[(': 
      stack.append(ch)
      continue

    if ch in ')]':
      if not stack: return False
      if stack.pop() + ch not in ['()', '[]']:
        return False
  
  return not len(stack)

while (text := input()) != '.':
  print(['no', 'yes'][check_brackets(text)])
