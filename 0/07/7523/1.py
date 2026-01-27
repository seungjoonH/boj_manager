_,*a=map(str.split,open(0))
def f(x,y):return(x+y)*(y-x+1)//2
print('\n\n'.join([f'Scenario #{i+1}:\n{f(*map(int,t))}'for i,t in enumerate(a)]))