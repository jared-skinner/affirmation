import sql_interface
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():

    sql.add_comment("You are the best!")
    sql.add_comment("It has been good to know you!")
    sql.add_comment("Those are some fancy pants!")

    affirmations = sql.get_comments()

    #print(affirmations)

    return render_template('index.html', affirmations = affirmations)

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
    sql = sql_interface.SQL()

    sql.create_comments_table()

    app.run()



