n, k = map(int, input().split())
l = [i for i in range(1, n + 1) if not (n % i)]
print(0 if len(l) < k else l[k - 1])
