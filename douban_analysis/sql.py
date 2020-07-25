import pymysql

class Mysql_Control:

    def __init__(self):
        pass

    def connect(self):
        conn = pymysql.connect(host="127.0.0.1", user="root",password="5381808",database="yingping",charset="utf8")
        return conn

    
    def insert_db(self, table_name, text):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "INSERT INTO {}(text) VALUES ( %s);".format(table_name)
        try:
            cursor.execute(sql,[text])
            conn.commit()
        except Exception as e:
            print(e)
            conn.rollback()
        cursor.close()
        conn.close()


    def select_db(self, table_name):
        conn = self.connect()
        cursor = conn.cursor()
        sql = "SELECT text from {};".format(table_name)
        cursor.execute(sql)
        ret = cursor.fetchall()
        cursor.close()
        conn.close()
        return ret


    def create_db(self, table_name):
        conn = self.connect()
        cursor = conn.cursor()
        sql = """CREATE TABLE IF NOT EXISTS {}(id INT auto_increment PRIMARY KEY ,text text NOT NULL)ENGINE=innodb DEFAULT CHARSET=utf8;""".format(table_name)
        cursor.execute(sql)
        cursor.close()
        conn.close()