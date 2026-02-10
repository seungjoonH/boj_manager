import re
_,*a=open(0)
f=lambda x:bool(re.search(r'(01|OI)',x))
print(sum(map(f,a)))