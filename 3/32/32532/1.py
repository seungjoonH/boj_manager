s=input;o,t=s()[15:-4],s()[:6];y,m,d=[t[i:i+2]for i in[0,2,4]]
f,l,*_=map(lambda x:x[0]+x[1:].lower(),s().split('<<')[:2])
print('Ime:',f+'\nPrezime:',l+'\nDatum rodjenja:',f'{d}-{m}-{19+(y<"25")}{y}\nOIB:',o)