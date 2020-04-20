# -*- coding:utf-8 -*-
import json, config
## libraries
import pyodbc
import pandas as pd


sv=config.server
db=config.database
un=config.username
pw=config.password

print('***Azure SQL Database connect {}'.format(sv))
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+sv+';DATABASE='+db+';UID='+un+';PWD='+ pw)
cursor = conn.cursor()


sql = 'SELECT * FROM tblMM;' 
print('***SQL--- {}'.format(sql))
df = pd.read_sql(sql, conn)
print(df.head(100))

