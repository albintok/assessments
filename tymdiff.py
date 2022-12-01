# lst1=[]
# lst2=[]
# lst3=[]
# data= "06AM-12PM,11AM-02PM,07AM-02PM,08AM-02PM,08AM-03PM,11AM-05PM,12PM-06PM,01PM-07PM,02PM-08PM,03PM-09PM,03PM-10PM"
# data1=(data.split(','))
# for i in data1:
#     lst1.append(i[0:2])
#     lst2.append(i[5:7])
# print(lst1)
# print(lst2)
# for i in range(0,len(lst1)):
#     if int(lst1[i])>int(lst2[i]):
#         lst3.append(int(lst1[i]) - int(lst2[i]))
#     else:
#         lst3.append(int(lst2[i])-int(lst1[i]))
# print(lst3)
# newlst=[]
# res=[]
# data= "6AM-12PM,11AM-2PM,7AM-2PM,8AM-2PM,8AM-3PM,11AM-5PM,12PM-6PM,1PM-7PM,2PM-8PM,3PM-9PM,3PM-10PM"
# data1=(data.split(','))
# for i in data1:
#     lst=str(i)
#     lst1=lst.split('-')
#     for j in lst1:
#         newlst.append(j[:-2])
# start=newlst[::2]
# end=newlst[1::2]
# for i in range(0,len(start)):
#     if int(start[i])>int(end[i]):
#         res.append(int(start[i]) - int(end[i]))
#     else:
#         res.append(int(end[i])-int(start[i]))
# print(res)
import datetime
data= "6AM-12PM,11AM-2PM,7AM-2PM,8AM-2PM,8AM-3PM,11AM-5PM,12PM-6PM,1PM-7PM,2PM-8PM,3PM-9PM,3PM-10PM"

df=data.strip().split("\n")
print(df)
col=[i.split(',')for i in df]
print(col)
time=col[0]
print(time)

hr=[tm.split('-') for tm in time]
print(hr)

fmt='%I%p'
print(fmt)
hour=[abs(int((datetime.datetime.strptime(i[1],fmt)-datetime.datetime.strptime(i[0],fmt)).total_seconds()/(60*60))) for i in hr]
print(hour)