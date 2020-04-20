# -*- coding:utf-8 -*-
import json, config
from requests_oauthlib import OAuth1Session
## libraries
import pyodbc


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
tweet = '現在のレコード総数は  です'
print('-------------------------------')

#パラメータのセット
params = {"status" : tweet}

req = twitter.post(url, params = params)

if req.status_code == 200:
    #正常に処理できたら
    print("Success!")
else:
    print("ERROR : %d" % req.status_code)
