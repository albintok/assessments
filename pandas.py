# 1.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print(df.to_string())

# 2.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# columns=["Duration","Pulse"]
# print(df[columns].head(6))

# 3.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print(df["Duration"])
#
# 4.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# color=pd.NaT
# df['colour']=color
# print(df)
# #
# 5.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print(df.shape)
# print(df.dtypes)
#
 # 6.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# df.rename(columns={"Duration":"durate","Maxpulse":"Max"},inplace=True)
# print(df)
#
# 7.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before removing ")
# print(df.head())
# #
# # df.drop("Pulse",axis=1,inplace=True)
# # print("after removing ")
# # print(df.head())
#
#
# #or
# df.pop("Pulse")
# print("after removing ")
# print(df.head())

# 8.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before removing ")
# print(df.head())
#
# df.drop(["Pulse","Calories"],axis=1,inplace=True)
# print("after removing ")
# print(df.head())
#
#
# # #or
# # df.pop(["Pulse","Calories"])
# # print("after removing ")
# # print(df.head())

# 9.

# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before removing ")
# print(df.head())
#
# df.drop([1,2,3],axis=0,inplace=True)
# print("after removing ")
# print(df.head())

# 10.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before removing ")
# print(df.head())
#
# new=df.Pulse.sort_values(ascending=True)
# print("after sorting only 1 column ")
# print(new)

# 11.

# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before removing ")
# print(df.head())
#
# df.sort_values(["Pulse"],axis=0,inplace=True,ascending=[True])
# print("after sorting ")
# print(df.head())

# 12.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before removing ")
# print(df.head())
#
# df.sort_values(["Maxpulse"],axis=0,inplace=True,ascending=[False])
# print("after sorting ")
# print(df.head())

# 13.

# import pandas as pd
# l=[1,2,3,4,5]
# print(l)
# df=pd.Series(l)
# print(df)

# 14.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before filter")
# print(df.head())
#
# result=df[(df.Pulse>=120) &(df.Maxpulse>=150)]
# print(result)
#
# # 15.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before filter")
# print(df.head())
#
# result=df[(df.Pulse>=120) | (df.Maxpulse>=150)]
# print(result)
#
# 16.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before filter")
# print(df.head())
#
# print(df.columns)
#
# # 17.
# import pandas as pd
# df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
# print("before filter")
# print(df.head())
# for index,row in df.iterrows():
#   print(index,row.Duration,row.Pulse)

# 18.
import numpy as np
import pandas as pd
df = pd.read_csv(r'C:\Users\HP\Downloads\data.csv')
print("before filter")
print(df.head())
print(df.select_dtypes(include=[np.number]).dtypes)