import sqlite3
from sqlite3 import Error
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    select_task_by_priority(1)

    return render_template('index.html')

@app.route('/manage')
def manage():
    return render_template('manage.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/approval')
def approval():
    return render_template('approve.html')













 
 
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
 
 
def select_all_tasks():
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_task_by_priority(priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE priority=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
        #print("1. Query task by priority:")
        #select_task_by_priority(conn,1)
# 
#        print("2. Query all tasks")
#        select_all_tasks(conn)
 
 

if __name__ == '__main__':
    database = "test.db"
 
    # create a database connection
    conn = create_connection(database)

    app.run()



