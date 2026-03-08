_, *a = map(str.strip, open(0))
for s in a: print('The number of vowels in', s, f'is {sum(c in 'aeiou' for c in s)}.')