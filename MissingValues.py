#!/usr/bin/env python
# coding: utf-8

# In[2]:


def numeric_na_replace(data):
    numcols = data.select_dtypes(exclude="O").columns
    print("Numeric Columns:")
    print(numcols)
    print()
    print("Missing Values Count for Each Column:")
    print(data[numcols].isnull().sum())
    print("Replacing Na Values With Column Median value........")
    print()
    for col in numcols:
        data[col].fillna(round(data[col].median()), inplace=True)    
    print("Missing Values Count for Each Column:") 
    display(data[numcols].isnull().sum())
    
def categorical_na_replace(data):
    catcols = data.select_dtypes(include="O").columns
    print("Categorical Columns:")
    print(catcols)
    print()
    print("Missing Values Count for Each Column:")
    print(data[catcols].isnull().sum())
    print("Replacing Na Values With Column Mode value........")
    print()
    for col in catcols:
        data[col].fillna(data[col].mode()[0], inplace=True)    
    print("Missing Values Count for Each Column:") 
    display(data[catcols].isnull().sum())
    
def categorical_na_replace_withref(data, parentcol, childcol):
    display(data[childcol].isnull().sum())
    print("Replacing Na Values with ref to given column......")
    for cls in data[parent].unique():
        if data[(data[parent]==cls)&(data[child].isnull())] is not None:
            indexes = data[(data[parent]==cls)&(data[child].isnull())].index
            try:
                val = data[data[parent]==cls][child].mode()[0]
                data[child].iloc[indexes] = val
                print(cls)
                print(val)
                print()
            except:
                print(cls)
                print("Class data is not having proper replacement values:")
#                 data[child].iloc[indexes] = input("Enter Value of Ur Choice:")
                data[child].iloc[indexes] = 'notgiven'
                print()
    
    display(data[childcol].isnull().sum())




