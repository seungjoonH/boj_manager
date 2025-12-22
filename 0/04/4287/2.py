d = lambda t: chr(((ord(t[2]) - 97) + (ord(t[1]) - ord(t[0]))) % 26 + 97)
while (i:=input()) != '#': print(*i.split(), ''.join(map(d, zip(*i.split()))))