n, y = map(int, input().split())
o = set([int(input()) for _ in range(y)])
m = [i for i in range(n) if i not in o]
print(*m, f'Mario got {len(o)} of the dangerous obstacles.', sep='\n')