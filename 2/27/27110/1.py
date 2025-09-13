m, nums = map(str.strip, open(0))
mn = lambda x: eval('min(%s, %s)' % (x, m))
print(sum(map(mn, nums.split())))