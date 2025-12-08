import re
for _ in'   ':print(max(len(s)for s,_ in re.findall(r'((\d)\2*)',input())))