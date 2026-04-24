d=('ABCDEFGHJLM ACEFGHILM ACEFGHILM ABCEFGHLM '+('ACEFGHLM '*5)+'ABCFGHLM').split()
x=d[int(input())-1]
print(len(x))
print(*x)