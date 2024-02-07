#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
'''
data1 = {'emp':['krishna', 'avinash'],
        'dept': ['IT', 'Admin']}

data2 = {'deptname': ['Information technology', 'Adminstration'],
         'dept': ['IT', 'Admin']}

df_data1 = pd.DataFrame(data1).to_csv("a")
df_data2 = pd.DataFrame(data2).to_csv("b")
'''
df_data1=pd.read_csv(r"C:\Users\Plabani\Downloads\chk\a.csv")
df_data2=pd.read_csv(r"C:\Users\Plabani\Downloads\chk\b.csv")


df_data1.merge(df_data2, on = 'dept').to_csv(r"C:\Users\Plabani\Downloads\chk\x.csv")

#print(df_data1.count())
print(len(df_data1) == len(df_data2))


# In[ ]:




