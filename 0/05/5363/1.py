for _ in range(int(input())):
  sentence = input().split()
  print(*sentence[2:], *sentence[:2])