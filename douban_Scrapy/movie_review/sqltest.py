# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(host="127.0.0.1", user="root",password="5381808",database="yingping",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
table_name = "USER2"
# 定义要执行的SQL语句
sql = """CREATE TABLE {} (id INT auto_increment PRIMARY KEY ,name CHAR(10) NOT NULL UNIQUE,age TINYINT NOT NULL)ENGINE=innodb DEFAULT CHARSET=utf8;""".format(table_name)
# 执行SQL语句
cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()