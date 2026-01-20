import re
print(len(re.findall(r'3|6|9',''.join(map(str,range(1+int(input())))))))