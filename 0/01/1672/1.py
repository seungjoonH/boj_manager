input();s=input()
while len(s)>1:a,b=map('ACGT'.index,sorted(s[-2:]));s=s[:-2]+'AACGCTGGAT'[b+4*a-a*-~a//2]
print(s)