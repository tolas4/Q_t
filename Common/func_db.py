import pymysql
from Common.func_option import conf


class ConnDB:

    def __init__(self):
        self.conn = pymysql.connect(
            host=conf.get("nmb_db", "host"),
            user=conf.get("nmb_db", "user"),
            port=conf.getint("nmb_db", "port"),
            database=conf.get("nmb_db", "database"),
            password=conf.get("nmb_db", "password"),
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )
        self.cur = self.conn.cursor()

    def select_one(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def select_all(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def update(self, sql):
        self.cur.execute(sql)
        self.conn.commit()

    def get_acount(self, sql):
        self.conn.commit()
        return self.cur.execute(sql)

    def close_db(self):
        self.cur.close()
        self.conn.close()