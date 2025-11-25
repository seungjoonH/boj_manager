m, d = map(int, open(0))
print(["Before", "After", "Special"][(m>2 or m>=2 and d>=18) + (m==2 and d==18)])