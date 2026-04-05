n,*a=map(int,input().split())
print('\n'.join([('v.'*n)[i:i+n]for i in range(-~n//2<<1)][::1-sum(a)%2*2][:n]))