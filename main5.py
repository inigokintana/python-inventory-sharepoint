import os
from pandasql import sqldf
import pandas as pd



def readXlsxfile():
    df = pd.read_excel(open(r'C:\\Users\\iquintza\\OneDrive - ELKARLAN\\Attachments\\test.xlsx', 'rb'), sheet_name='Hoja1', engine='openpyxl')  

    #xlsx
    #df = pd.read_excel(bytes_file_obj, engine='openpyxl')
    #xls
    #df = pd.read_excel(bytes_file_obj, engine='xlrd')
        
    print(df)
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html
    # https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/03_subset_data.html
    
    # search 1 in DF
    over_hiru = df[df["Value"] > 3]
    print(over_hiru)
    
    # search 2 in DF
    lau= df[df["Name"] =="Lau"]
    print(lau)
    
    # Search 3 in DF using AND
    biggerBost=df[(df["Name"] !="bost") & (df["Value"] >= 5)]
    print(biggerBost)
    
    # Search 4 in DF using SQL
    print(sqldf('''SELECT Name, Value 
    FROM df 
    WHERE Name!="bost" AND Value>=5 '''))
    
    print(sqldf('''SELECT "Etiqueta de activo"
    FROM df 
    WHERE Category="PC" '''))
    
    
    


if __name__ == "__main__":
  readXlsxfile()