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
    cols2change = {'description':'order_description','val/coarea_crcy':'cost_kob','dr/cr_indicator':'indicator'}

    df.rename(index = str, columns = cols2change,inplace = True)
    '''
    print(df.columns)
    df.rename(index = str, columns = cols2change , inplace = True)
    print(df.columns)
    return(df)

def cols2drop(df,cols):
    '''
    cols2drop = ['co_object_name','cost_element']
    populate cols2drop list with column names as shown in the sample above.
    
    df = cols2drop(df,cols)
    '''
    print('columns before droppping')
    print(df.shape)
    print(df.columns)
    df.drop(cols,axis =1, inplace = True)
    print('coluns after dropping')
    print(df.shape)
    print(df.columns)
    return(df)

print('reading excel sheets......')

material = readxl('material','Legacy_material_dump.xlsx')
order = readxl('order','Legacy_WO_dump.xlsx')


cols2 = ['plant','order_type','actual_date','quanity', 'uom','quantity_returned', 'posting_date']
material = cols2drop(material,cols2)

cols3 = ['plnt','order_finish_date', 'p','equipment','system_statu', 'user_statu', 'esttotcost', 'totcosplan', 'totcostact']
order = cols2drop(order,cols3)


print('list of column names of material data frame and renaming')
#print(material.columns)

material.rename(index = str, columns = {'description':'description_other'}, inplace = True)
#print(material.columns)

print('list of column names of order data frame and renaming')
#print(order.columns)

order.rename(index = str, columns = {'type':'order_type'}, inplace = True)
#print(order.columns)

print('dropping rows where material number is not there')
print('material dataframe shape before')
print(material.shape)
material = material[np.isfinite(material['material'])]
print('material dataframe shape after')
print(material.shape)

print('sortng material df')
material.sort_values(by = ['order', 'material'],inplace = True)
print(material.columns)
print(order.columns)

order = order.reindex(columns = ['functional_location', 'floc_description',
                                 'order_type','order','short_text',
                                 'order_start_date'])


print('sorting order df')
order.sort_values(by = ['functional_location','order'],inplace = True)

print(order.columns)

df = order.merge(material, on = 'order', how = 'outer')
print(df.columns)
print(df.shape)
print(order.shape)
print(material.shape)

newcols = ['material','material_description','functional_location',
           'floc_description', 'order','order_type',
            'short_text','description_other', 'order_start_date']

df = df.reindex(columns = newcols)
print(df.columns)
print(df.shape)
df = df[np.isfinite(df['material'])]

df = df[np.isfinite(df['order'])]
df.sort_values(by = ['functional_location','order','material'], inplace = True)
print(df.shape)


df2 = df.copy()
df2 = df2.set_index(['material','material_description','functional_location','floc_description','order'])
rite2xl(df2,'csl_legacy.xlsx')
#rite2xl(df,'legacy_unmerged.xlsx')
'''
print(df2.shape)


print(' continue using df for further data manipulations......')
print(df.shape)

print(' earlier start date to datetime format')

df['earl_start_date'] = pd.to_datetime(df['earl_start_date'],format = '%d%b%Y')
print(df.head())

print(df.columns)

x = set(df.movement_type)
print(x)

#print(df.na_count <-sapply(x, function(y) sum(length(which(is.na(y))))))

print(np.where(pd.isnull(df['order'])))

print(df.shape)
df = df[np.isfinite(df['order'])]
print(df.shape)

df = df.reindex(columns=  ['funcloc', 'funclocdesc', 'order', 'description_ord', 'opr_short_text',
       'material', 'description_mat', 'movement_type', 'order_type',
       'total_act_cost', 'amount_in_lc', 'earl_start_date'])

print(df.columns)

df6 = df.copy()

print(df6.columns)
#the below indexgroups list was used for try1.xlsx
#indexgroups =['funcloc', 'funclocdesc', 'order', 'description_ord','opr_short_text','material', 'description_mat']

#below index groups used for try2.xlsx
#indexgroups =['funcloc','funclocdesc', 'order','description_ord','opr_short_text','material','description_mat','movement_type','earl_start_date']

#below index groups used for try3.xlsx
indexgroups =['funcloc','funclocdesc', 'order','description_ord','material','description_mat','total_act_cost', 'amount_in_lc','opr_short_text']


#below index groups used for try5.xlsx
indexgroups =['funcloc','funclocdesc', 'order','description_ord','material','description_mat']
#index = pd.MultiIndex.from_product(indexgroups)



df6.set_index(indexgroups,inplace = True)

#df6['earl_start_date'] = pd.to_datetime(df6['earl_start_date'],format = '%d%b%Y')

#df6['date'] = df6['earl_start_date'].dt.date()

print(df6.head())
print(df6.columns)
print(df6.shape)

df6.drop(['movement_type', 'order_type'], axis = 1, inplace = True)

        

#df5 = df6.pivot_table( values = 'earl_start_date', index = ['funcloc', 'order','material', 'description_mat',])

print(df6.head())
#rite2xl(df6,'try4.xlsx')

df5 = df6.copy()
df5.drop(['opr_short_text','total_act_cost','amount_in_lc'], axis = 1, inplace = True)
#rite2xl(df5,'try5.xlsx')

'''
