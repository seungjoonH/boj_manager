from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
a = [int(input(), 2) for _ in range(n)]
b = [int(input(), 2) for _ in range(n)]
c = [0 for _ in range(n)]

def B(n): return ('{:>0'+ str(m) +'b}').format(n)
def p(): 
  print('==')
  print('\n'.join(list(B(i) for i in c)))
  print()


for i in range(n): c[i] = a[i] ^ b[i]

count = 0
for i in range(n - 2):
  for j in range(m - 1, 1, -1):
    pivot, sub = 1 << j, 7 << (j - 2)
    if pivot & c[i]:
      for k in range(3): c[i + k] ^= sub
      count += 1

print(-1 if sum(c) else count)

'''
3 4
0000
0010
0000
1001
1011
1001
'''

'''
4 7
1100000
0000011
0011111
0000011
1111011
1110100
1101000
1101111
'''

'''
1 1
1
1
'''

'''
3 42
011001011111111100101000111111001010010111
111111011001011001001011000111011110111011
100101110101010111110100001001100110111110
011001010110000110010000111001100111000110
010010001100100111100010101000101101010100
101111100111000010111000110011001111100011
'''

'''
2 2
00
00
11
11
'''

'''
3 4
1110
1110
1110
0001
0001
0001
'''


'''
1 1
0
0
'''