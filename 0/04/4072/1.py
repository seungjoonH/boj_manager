while (s := input()) != '#':
  print(*(x[::-1] for x in s.split()))