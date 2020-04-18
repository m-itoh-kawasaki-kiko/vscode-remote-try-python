# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session
## libraries
import pyodbc

## 関数定義
### DB connectionを定義
def db_connection(sv=config.server, db=config.database, un=config.username, pw=config.password):    
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+sv+';DATABASE='+db+';UID='+un+';PWD='+ pw)
    return cnxn.cursor()

### SQLを発行
def query_output(sql):
    cursor.execute(sql)
    row = cursor.fetchone()
    while row:  
        print(row[0])  
        result = row[0]
        row = cursor.fetchone()
    return result

### DB connectionしときます
cursor = db_connection()

### SalesLT.Customerはテンプレートとしてあるテーブル
sql = 'select count(*) from tblMM;' 
maxcnt = query_output(sql)

#Twitter
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK,CS,AT,ATS)

url = "https://api.twitter.com/1.1/statuses/update.json"

#投稿内容入力
#print("呟く内容は？")
#tweet = input('>> ')
tweet = '現在のレコード総数は ' + str(maxcnt) + ' です' + '\r\n'
tweet += '*** Automatic response with Python ***'
print('-------------------------------')

#パラメータのセット
params = {"status" : tweet}

req = twitter.post(url, params = params)

if req.status_code == 200:
    #正常に処理できたら
    print("Success!")
else:
    print("ERROR : %d" % req.status_code)
