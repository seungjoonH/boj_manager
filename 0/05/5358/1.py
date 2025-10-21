l = map(str.strip, open(0))
def change(s): return s.translate(str.maketrans("eiEI", "ieIE"))
print(*map(change, l), sep='\n')