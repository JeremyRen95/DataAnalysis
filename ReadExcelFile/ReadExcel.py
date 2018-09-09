import pandas as pd

df = pd.read_excel('data.xlsx')
#aa = df.drop('张三',axis=0)
#bb = df.replace({'female':1,'male':0})
#print(aa)
#print(bb.values)
print(df.values)