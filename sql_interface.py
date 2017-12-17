import sqlite3
from sqlite3 import Error

class SQL():
    def __init__(self):
        self.conn = self.create_connection("affirmation.db")
        self.cur = self.conn.cursor()

    def create_connection(self, db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)

        return None


    def dict_factory(self, row):
        d = {}
        for idx, col in enumerate(self.cur.description):
            d[col[0]] = row[idx]
        return d


    def get_comments(self, approved = "ALL"):
        """
        Query tasks by priority
        :param conn: the Connection object
        :param priority:
        :return:
        """

        if approved == "ALL":
            query = "SELECT * FROM comments;"
        elif approved == "0" or approved == "1":
            query = "SELECT * FROM comments WHERE approved = " + approved + ";"
        else:
            return False

        self.cur.execute(query)

        rows = self.cur.fetchall()

        comments = []
        for row in rows:
            comments.append(self.dict_factory(row))

        return comments


    def update_status(self, id, status):
        query = 'UPDATE comments SET approved = ' + status + ' where id = ' + id + ';'

        try:
            self.cur.execute(query)
        except Error as e:
            print(e)


    def create_comments_table(self):
        query = '''
            CREATE TABLE
            IF NOT EXISTS comments (
                 id INTEGER PRIMARY KEY,
                 comment TEXT NOT NULL,
                 approved INTEGER DEFAULT 0
            );'''

        try:
            self.cur.execute(query)
        except Error as e:
            print(e)


    def add_comment(self, comment):
        query = "INSERT into comments ( comment ) VALUES ('" + comment + "');"
        try:
            self.cur.execute(query)
        except Error as e:
            print(e)

