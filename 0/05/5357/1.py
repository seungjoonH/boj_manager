import re
for s in[*open(0)][1:]:print(*re.sub(r'(.)\1+',r'\1',s.strip()),sep='')