_,*a=map(str.split,open(0))
print(*map(lambda x:f'$%.2f'%eval(x),map('*'.join,a)),sep='\n')
