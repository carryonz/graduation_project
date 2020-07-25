import csv
import pymysql
import numpy as np


conn = pymysql.connect(host="127.0.0.1", user="root",password="5381808",database="yingping",charset="utf8")
with open('./data/review.csv', 'r', encoding='UTF-8') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
# 将读取出来的语料转为list
review_data = np.array(rows).tolist()
review_list = []
sentiment_list = []
# 第一列为差评/好评， 第二列为评论
for words in review_data:
    cursor = conn.cursor()
    sql = "INSERT INTO top250(sentiment,review) VALUES (%s, %s);"
    try:
        cursor.execute(sql,[words[0], words[1]])
        conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    cursor.close()
conn.close()


