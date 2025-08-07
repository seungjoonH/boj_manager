while True:
  name, age, weight = input().split()
  if name == '#': break
  print(name, ['Junior', 'Senior'][int(age) > 17 or int(weight) >= 80])
