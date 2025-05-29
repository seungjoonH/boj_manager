import re

while (text := input()) != '.':
  pattern = re.compile(r'[^\(\)\[\]]')
  text = re.sub(pattern, '', text)
  repl = text
  
  while repl:
    repl = repl.replace('()', '').replace('[]', '')
    if text == repl: break
  
  print(['no', 'yes'][repl == ''])