a=input()
print(eval('+'.join(a[-i:]+a[:-i]for i in range(len(a)))))