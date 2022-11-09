import file3 as pd
dct = pd.DataFrame({'Electronics' : pd.Series([97, 56, 87, 45], index =['John', 'Abhinay', 'Peter', 'Andrew']),
   'Civil' : pd.Series([97, 88, 44, 96], index =['John', 'Abhinay', 'Peter', 'Andrew'])})

dct['mean'] = dct.mean(axis=1)
print(dct.head())
x = len(dct['mean'])
a = []
for i in range(x):
   if dct['mean'][i]>90:
      a.append('A')
   elif dct['mean'][i]>80:
      a.append('b')
   elif dct['mean'][i] >70:
      a.append('c')
   elif dct['mean'][i]>60:
      a.append('D')

print(a)
dct['grade'] =  a
print(dct)