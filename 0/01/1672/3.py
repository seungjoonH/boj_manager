input();s=[*input()]
while len(s)>1:a,b=map('AGCT'.index,[s.pop(),s.pop()]);s.append('ACAGCGTAATCGGAGT'[4*a+b])
print(*s,sep='')