import datetime

a,b = input().split()
a = int(a)
b = int(b)
day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
answer = day[datetime.datetime(2007,a,b).weekday()]
print(answer)