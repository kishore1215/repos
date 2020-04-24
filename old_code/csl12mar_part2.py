import pandas as pd
import numpy as np
import pickle
import datetime as dt
'''
df  = pd.read_excel('ref_csl.xlsx',sheet_name = 'Sheet1')

print(df.columns)
print(df.shape)

df1 = df.set_index(['material','order','funcloc'])

writer = pd.ExcelWriter('r2.xlsx', engine = 'xlsxwriter')
df1.to_excel(writer,'Sheet1')
writer.save()
print('printing to excel completed')

for a in ['funcloc']:
    for b in ['order']:
        for c in ['material']:
            print((a,b,c),df['earl_start_date'].min())

'''
df  = pd.read_excel('ref_csl.xlsx',sheet_name = 'Sheet1')
df.sort_values(by = ['material','funcloc','order'], inplace = True)
print(df.columns)
print(df.shape)

writer = pd.ExcelWriter('test.xlsx', engine = 'xlsxwriter')
df.to_excel(writer,'Sheet1')
writer.save()

df1 = df.set_index(['material','description_mat','funcloc','funclocdesc','order','order_type'])


writer = pd.ExcelWriter('testresult.xlsx', engine = 'xlsxwriter')
df1.to_excel(writer,'Sheet1')
writer.save()
print('printing to excel completed')



