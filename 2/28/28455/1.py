n,*a=map(int,open(0))
a=sorted(a)[-42:]
def f(l):return 5-(l<60)-(l<100)-(l<140)-(l<200)-(l<250)
print(sum(a),sum(map(f,a)))