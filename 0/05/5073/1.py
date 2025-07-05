def triangle(a, b, c):
  if a + b <= c: return "Invalid"
  if a == b == c: return "Equilateral"
  if a == b or b == c: return "Isosceles"
  return "Scalene"

while True:
  s = (a, b, c) = tuple(map(int, input().split()))
  if not (a | b | c): break
  print(triangle(*sorted(s)))