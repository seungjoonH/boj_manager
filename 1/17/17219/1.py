from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
memory = dict()

for _ in range(n):
  address, password = input().split()
  memory[address] = password

for _ in range(m): print(memory[input().rstrip()])