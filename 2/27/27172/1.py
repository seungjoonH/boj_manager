from sys import stdin
input = stdin.readline

n = int(input())
cards = list(map(int, input().split()))
indices = dict((card, i) for i, card in enumerate(cards))
mx = max(cards)
scores = [0] * n

for i in range(n):
  num = cards[i]
  target = num * 2

  while target <= mx:
    if not target % num and target in indices:
      scores[i] += 1
      scores[indices[target]] -= 1

    target += num

print(*scores)