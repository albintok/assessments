from datetime import datetime

x=input("enter the date and time")
y=(datetime.strptime(x,'%d/%m/%Y %H:%M'))
print(y.strftime("%b,%A,%d,%Y,%I:%M %p"))


