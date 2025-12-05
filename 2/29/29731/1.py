promises = ['Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop']

print(['Yes', 'No'][all(map(lambda x: x in promises, [*map(str.strip, open(0))][1:]))])