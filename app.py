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


def fetch_comments():
    pass


# TODO: make sure user has permissions
@app.route('/manage')
def manage():

    affirmations = sql.get_comments()
    return render_template('manage.html', affirmations = affirmations)


# TODO: make sure user has permissions
def update_comment_status():
    pass


# TODO: make sure user has permissions
def delete_comment():
    pass


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/add_affirmatoin')
def add_affirmation():
    sql.add_comment("You are the best!")
    return render_template('add.html')


@app.route('/approval')
def approval():

    affirmations = sql.get_comments()

    return render_template('approve.html', affirmations = affirmations)


if __name__ == '__main__':
    database = 'test.db'
 
    # create a database connection
    sql = sql_interface.SQL()

    sql.create_comments_table()

    app.run()

