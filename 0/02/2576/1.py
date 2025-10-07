l = [*filter(lambda x: x % 2, map(int, open(0)))]
print(f'{sum(l)}\n{min(l)}' if l else -1)