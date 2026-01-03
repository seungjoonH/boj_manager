s,k=map(str.rstrip,open(0))
print(''.join(c==' 'and c or chr(97+(ord(c)-ord(k[i%len(k)])-1)%26)for i,c in enumerate(s)))