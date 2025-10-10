l=[*map(int,input().split())]
print(["none","draw","hacker"][~-all(x<=int(y)*100for x,y in zip(l,'112233445'))or 99<sum(l)])