import sql_interface
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    sql_interface.get_comments(1)

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


if __name__ == '__main__':
    database = 'test.db'
 
    # create a database connection
    conn = sql_interface.create_connection(database)

    sql_interface.create_comments_table()

    app.run()



