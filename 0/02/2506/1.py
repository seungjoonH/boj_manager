def f(x):n=len(x);return(n+1)*n//2
input();print(sum(map(f,filter(bool,input().replace(' ', '').split('0')))))