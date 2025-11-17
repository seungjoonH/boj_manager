import re
_,*a=open(0);print(max(len(re.findall('for|while',i))for i in a))