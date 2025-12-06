input();s=input()
while len(s)>1:a,b=map('AGCT'.index,s[-2:]);s=s[:-2]+'ACAGCGTAATCGGAGT'[4*a+b]
print(s)