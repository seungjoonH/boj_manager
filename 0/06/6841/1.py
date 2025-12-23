d = {
  'CU': 'see you',
  ':-)': 'I’m happy',
  ':-(': 'I’m unhappy',
  ';-)': 'wink',
  ':-P': 'stick out my tongue',
  '(~.~)': 'sleepy',
  'TA': 'totally awesome',
  'CCC': 'Canadian Computing Competition',
  'CUZ': 'because',
  'TY': 'thank-you',
  'YW': 'you’re welcome',
  'TTYL': 'talk to you later'
}

print(*[d[i] if i in d else i for i in map(str.strip, open(0))], sep='\n')