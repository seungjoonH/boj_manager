people = list(map(int, input().split()))
apple, _, __ = map(int, input().split())
print(apple in people and 1 + people.index(apple) or 0)