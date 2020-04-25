import pandas as pd
import numpy as np
import pickle
import datetime as dt


def readxl(df, file_name):
    """
    This function is to read excel sheets in to data frame
    It strips white spaces
    converts column names to lower case
    returns a dataframe
    function calling syntax should be carefully used as below

    cost = readxl('cost','cost.xlsx')

    """
    print( 'reading the excel file') 
    df = pd.read_excel(file_name, sheet_name = 'Sheet1')
    df.columns = [x.strip('/s+').lower().replace(' ','_').replace('.','_') for x in df.columns]
    print('list of columns of data frame ')
    print(df.columns)
    print('shape of data frame')
    print(df.shape)
    print('reading excel file completed')
    return(df)

def rite2xl(df, file_name):
    """
    function to convert data frame to excel sheet
    use syntax as shown below for execution

    result = rite2xl(result,'result.xlsx')
    
    """
    print('writing dataframe to excel',)
    writer = pd.ExcelWriter(file_name ,engine = 'xlsxwriter')
    df.to_excel(writer,file_name)
    writer.save()
    print('writing to excel sheet completed')
    return(df)
    
def colrename(df,cols2change):

    '''
    cols2change is a dictionary you want to change the column names
    populate cols2change dictionary before using this function


    '''
    print(df.columns)
    df.rename(index = str, columns = cols2change , inplace = True)
    print(df.columns)
    return(df)

def cols2drop(df,cols):
    '''
    cols2drop = ['co_object_name','cost_element']
    populate cols2drop list with column names as shown in the sample above.
    '''
    print('columns before droppping')
    print(df.shape)
    print(df.columns)
    df.drop(cols,axis =1, inplace = True)
    print('coluns after dropping')
    print(df.shape)
    print(df.columns)
    return(df)

print(' reading excel sheet with data of dsl kob report with parent FL mapped')



df = readxl('df','kob2mar.xlsx')

source = df.copy()

print(df.head())
print('size of data frame:')
print(df.size)
print('shape of data frame: ')
print(df.shape)
print('col names:')
print(df.columns)

data1 = df.copy()

cols2change = {'co_object_name' : 'description1',
                'val/coarea_crcy':'cost_kob',
               'material' : 'material_no',
               'dr/cr_indicator' : 'indicator',
               'cost_element_name' : 'description2',
               'name' : 'description3'}

colrename(df,cols2change)
              
cols = ['cost_element','period','vendor_name','total_quantity','user_name']

df = cols2drop(df,cols)

print(type(df['posting_date']))

print('converting posting_date to pandas date time')

df['posting_date'] = pd.to_datetime(df['posting_date'],format = '%d%b%y')

print(df.head())

print(type(df['posting_date']))

df['year'] = df['posting_date'].dt.year

print(df.columns)

print('dropping posting date after extracting year information')

cols2 = ['posting_date']
df = cols2drop(df,cols2)

print('re arranging columns')
df = df[['parent_floc','order','material_no',
        'material_description','description1',
        'description2','description3',
        'indicator','year','cost_kob']]

print(df.columns)

print('setting  multi index')

df.sort_values(['parent_floc','order','material_no'], inplace = True)

df.set_index(['parent_floc','order','material_no'], inplace = True)

#rite2xl(df,'try1.xlsx')

#print(df.head())

print(df.columns)

print(df.describe())

df_pivot = pd.pivot_table(df,values = 'cost_kob',index = ['parent_floc','order','material_no'], columns = 'year', aggfunc = 'sum')

#rite2xl(df_pivot,'try2.xlsx')

df_des1 = df.groupby(['parent_floc','order','material_no']).cost_kob.sum()

#rite2xl(df_des1,'try3.xlsx')













