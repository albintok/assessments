count={}
f=open("text.txt",'r')
s=f.read()
for i in s:
    if i not in count:
        count[i]=1
    else:
        count[i]+=1
for k,v in count.items():
    print(k,":",v)