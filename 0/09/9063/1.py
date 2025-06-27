coords = [map(int, input().split()) for _ in range(int(input()))]
(x, y), dif = zip(*coords), lambda x: abs(max(x) - min(x))
print(dif(x) * dif(y))