import MySQLdb as mysql_db

class DBManager:
    def __init__(self):
        self.connection = None
        self.cursor = None
        
    def connect(self):
        try:
            self.connection = mysql_db.connect(
                host='localhost',
                user='root',
                passwd='@Thanh070891',
                db='medimanager',
                charset='utf8'
            )
            self.cursor = self.connection.cursor()
            return self.connection
        except Exception as e:
            print("Database connection failed:", e)
            return None

    def execute(self, query, params=None):
        self.cursor.execute(query, params or ())
        return self.cursor

    def executemany(self, query, params_list):
        self.cursor.executemany(query, params_list)
        return self.cursor

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def commit(self):
        self.connection.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
