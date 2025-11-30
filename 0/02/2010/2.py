import sys
sys.setrecursionlimit(10**6)
n,*a=map(str.strip,open(0));print(eval('+'.join(['1-'+n,*a])))