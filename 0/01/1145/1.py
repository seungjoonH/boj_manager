l = [*map(int, input().split())]
for i in range(min(l), 10 ** 10):
  if sum(map(lambda x: bool(i % x), l)) < 3: 
    print(i)
    break