print('int a;\nint *ptr = &a;')
for i in range(2,1+int(input())):print('int '+'*'*i+f'ptr{i} = &ptr{''if i<3else i-1};')