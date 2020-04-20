#---------------------------------------------------------------------
#ログイン
#接続文字列を作成してpyodbc.connectを実行すればログインができます。
# -*- coding: utf-8 -*-
import pyodbc
import pandas as pd

server = 'kwazure.database.windows.net'  
database = 'kwazuredbnis '  
username = 'FA00'  
password = 'K@w@s@ki1717'  

def login():
   
    connection = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ";uid=" + username + ";pwd=" + password + ";DATABASE=" + database
    # connection = "DRIVER={SQL Server};SERVER=" + server + ";uid=" + username + ";pwd=" + password + ";DATABASE=" + database

    return pyodbc.connect(connection)
#---------------------------------------------------------------------
#検索
#検索はログイン処理で取得したコネクションとSQLをselect_executeメソッドで処理しています。そして、取得したレコードをループし（１行しかありませんが）、各カラムの中身をprintしています。
def select_execute(con, slq):
        cursor = con.cursor()
        cursor.execute(slq)
        rows = cursor.fetchall()
        cursor.close()

        return rows

#---------------------------------------------------------------------
#更新
#NAMEカラムの中身を「ライン」から「ラインテスト」となるようにデータを更新します。要領は検索と同じですが、更新処理なので最後にcommitする必要があります。
def updatet_execute(con, slq):
    cursor = con.cursor()
    cursor.execute(slq)
    con.commit()
#---------------------------------------------------------------------
#挿入
#１レコード挿入する処理を書いています。
def insert_execute(con, slq):
    con.execute(sql,
                2,
                "ポイント",
                "マルチ",
                "特になし"
                )

    con.commit()
#---------------------------------------------------------------------
#削除
#上記処理で挿入したレコードを削除しています。
def delete_execute(con, slq):
    cursor = con.cursor()
    cursor.execute(slq)
    con.commit()



# if __name__ == '__main__':
#     con = login()

if __name__ == '__main__':
    con = login()
    # sql =  '''select *
    #             from tblMM'''
    #sql =  'SELECT TOP(20) * FROM tblMM ORDER BY dt DESC;' 
    sql =  """SELECT  * FROM tblMM WHERE code = 'TEST' ORDER BY dt DESC;""" 
    df = pd.read_sql(sql, con)
    print(df)
    
    # res = select_execute(con, sql)
    # for r in res:
    #     print(r[0], end=",")
    #     print(r[1], end=",")
    #     print(r[2], end=",")
    #     print(r[3])

# if __name__ == '__main__':
#     con = login()
#     sql = """UPDATE TEST
#                 SET NAME = NAME + 'テスト'"""

#     # データ更新
#     updatet_execute(con, sql)

# if __name__ == '__main__':
#     con = login()
#     sql = """INSERT
#              INTO TEST(FEATURE_NUM,
#                        NAME,
#                        TYPE,
#                        NOTE
#                        )
#                   VALUES (?,
#                           ?,
#                           ?,
#                           ?
#                           )"""

#     # データ登録
#     insert_execute(con, sql)

# if __name__ == '__main__':
#     con = login()
#     sql = """DELETE
#                FROM TEST
#               WHERE FEATURE_NUM = 2"""

#     # データ削除
#     delete_execute(con, sql)
