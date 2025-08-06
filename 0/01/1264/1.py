import re

while (i := input().lower()) != "#":
  print(len(re.findall(r'a|e|i|o|u', i)))