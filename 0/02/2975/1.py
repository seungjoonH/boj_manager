while (i := input()) != '0 W 0':
  res = eval(i.replace('W','-').replace('D','+'))
  print([res, 'Not allowed'][res < -200])