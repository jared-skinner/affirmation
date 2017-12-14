import sqlite3
from sqlite3 import Error

def create_connection(db_file):
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


def get_comments():
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM comments;")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
        #print("1. Query task by priority:")
        #select_task_by_priority(conn,1)
# 
#        print("2. Query all tasks")
#        select_all_tasks(conn)
 
 

def create_comments_table():
    create_table_sql = '''
        CREATE TABLE
        IF NOT EXISTS comments (
             id integer PRIMARY KEY,
             comment text NOT NULL
        );'''

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



