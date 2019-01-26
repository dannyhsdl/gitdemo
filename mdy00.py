import datetime
m=int(input("month: "))
d=int(input("date: "))
y=int(input("year: "))
i=datetime.datetime(y,m,d)
print(i)
n=i.strftime("%A")
print("it is ".title(),n)
print("Successfully finished.")