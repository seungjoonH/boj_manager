def check(s, l, r):
  while l < r:
    if s[l] != s[r]: return 0
    l += 1; r -= 1
  return 1

def palindrome(s):
  l, r = 0, len(s) - 1

  while l < r:
    if s[l] == s[r]: l += 1; r -= 1
    else: return 2 - (check(s, l + 1, r) or check(s, l, r - 1))

  return 0

_, *a = map(str.strip, open(0))
for i in a: print(palindrome(i))