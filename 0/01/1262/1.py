# #155
# n,a,b,c,d=map(int,input().split());r,m=2*n-1,n-1
# for i in range(a,c+1):print(''.join(chr(e+97if(e:=abs(i%r-m)+abs(j%r-m))<n else 46)for j in range(b,d+1)))

# #153
# n,a,b,c,d=map(int,input().split());r=2*n-1
# for i in range(a,c+1):print(''.join(chr(e+97)if(e:=abs(i%r-n+1)+abs(j%r-n+1))<n else'.'for j in range(b,d+1)))

# #151
# n,a,b,c,d=map(int,input().split());r=2*n-1
# for i in range(a,c+1):print(''.join(chr(46+(51+(e:=abs(i%r+1-n)+abs(j%r+1-n)))*(e<n))for j in range(b,d+1)))

##########

# #156
# n,a,b,c,d=map(int,input().split());r=2*n-1
# for i in range(a,c+1):print(''.join(chr(e%26+97)if(e:=abs(i%r-n+1)+abs(j%r-n+1))<n else'.'for j in range(b,d+1)))

# #154
# n,a,b,c,d=map(int,input().split());r=2*n-1
# for i in range(a,c+1):print(''.join(chr(46+((e:=abs(i%r+1-n)+abs(j%r+1-n))%26+51)*(e<n))for j in range(b,d+1)))

# #155
# n,a,b,c,d=map(int,input().split())
# for i in range(a,c+1):print(''.join(chr(46+((e:=abs(i%(r:=2*n-1)+1-n)+abs(j%r+1-n))%26+51)*(e<n))for j in range(b,d+1)))

# #154
# n,a,b,c,d=map(int,input().split());r=2*n-1
# for i in range(a,c+1):print(''.join(f'.{chr((e:=abs(i%r+1-n)+abs(j%r+1-n))%26+97)}'[e<n]for j in range(b,d+1)))

# 154
# n,a,b,c,d=map(int,input().split());r=2*n-1
# for i in range(a,c+1):print(''.join(('.'+chr((e:=abs(i%r+1-n)+abs(j%r+1-n))%26+97))[e<n]for j in range(b,d+1)))

# 154
# n,a,b,c,d=map(int,input().split());r=2*n-1
# for i in range(a,c+1):print(''.join(['.',chr((e:=abs(i%r+1-n)+abs(j%r+1-n))%26+97)][e<n]for j in range(b,d+1)))

# 153
n,a,b,c,d=map(int,input().split());r=2*n-1
for i in range(a,c+1):print(''.join(chr([46,(e:=abs(i%r+1-n)+abs(j%r+1-n))%26+97][e<n])for j in range(b,d+1)))


'''
4 1 1 7 7
5 3 18 10 46
20000 0 19980 10 20010
20000 19980 19940 19990 19980
'''