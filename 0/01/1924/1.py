from datetime import*
print(date(2007,*map(int,input().split())).ctime()[:3].upper())

m,d=map(int,input().split());print(['SUN','MON','TUE','WED','THU','FRI','SAT'][int(' 144025036146'[m])+d%7])