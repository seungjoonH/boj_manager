seed = int(input())
stocks = [*map(int, input().split())]

def bnp(seed, stocks):
  cash = seed
  held = 0

  for stock in stocks:
    buyable = cash // stock

    if not buyable: continue
    
    cash -= stock * buyable
    held += buyable

    if not cash: break

  return cash + stocks[-1] * held

def timing(seed, stocks):
  cash = seed
  held = acc = 0

  for i in range(1, len(stocks)):
    prev, curr = stocks[i - 1], stocks[i]
    dir = (curr > prev) - (curr < prev)

    if prev == curr: acc = 0
    elif acc * (curr - prev) < 0: acc = dir
    else: acc += dir
    
    if acc >= 3:
      if not held: continue
      cash += curr * held
      held = 0

    elif acc <= -3:
      buyable = cash // curr
      if not buyable: continue
      cash -= curr * buyable
      held += buyable

  return cash + stocks[-1] * held

b = bnp(seed, stocks)
t = timing(seed, stocks)

if b == t: print('SAMESAME')
else: print(['BNP', 'TIMING'][t > b])