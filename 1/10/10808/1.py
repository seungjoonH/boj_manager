m=[0]*26
for c in input():m[ord(c)-97]+=1
print(*m)