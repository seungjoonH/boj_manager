d = lambda t: chr(96 + (ord(t[1]) - ord(t[0]) + ord(t[2]) - 96) % 26)
while (i:=input()) != '#': print(*i.split(), ''.join(map(d, zip(*i.split()))))