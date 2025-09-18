def fact(n): return max(1, n and eval('*'.join(map(str, range(1, 1 + n)))))
print(fact(int(input())))