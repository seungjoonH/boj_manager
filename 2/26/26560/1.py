_, *a = map(str.strip, open(0))
for i in a: print(i if i[-1] == '.' else i + '.')